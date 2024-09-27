# modulo: faiss_index.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

# Configuración del logging para errores y depuración
log_file = "faiss_errors.log"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Cargar un modelo de embeddings pre-entrenado
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Función para crear un índice FAISS con IndexIVFFlat
def crear_indice_faiss(dimension_embedding, nlist=10):
    try:
        quantizer = faiss.IndexFlatIP(dimension_embedding)  # Cuantizador base
        index = faiss.IndexIVFFlat(quantizer, dimension_embedding, nlist, faiss.METRIC_INNER_PRODUCT)
        logging.debug(f"Índice FAISS creado correctamente con IndexIVFFlat, nlist: {nlist}")
        return index
    except Exception as e:
        logging.error(f"Error al crear el índice FAISS: {e}")
        return None

# Función para agregar fragmentos al índice
def agregar_fragmentos_a_faiss(index, fragmentos, ids):
    try:
        embeddings = model.encode(fragmentos)
        embeddings = np.array([emb / np.linalg.norm(emb) for emb in embeddings])
        logging.debug(f"Embeddings generados: {embeddings}")
        
        # Entrenar el índice antes de agregar embeddings
        index.train(embeddings)  # IndexIVFFlat requiere entrenamiento
        logging.debug("Índice FAISS entrenado correctamente.")
        
        index.add_with_ids(embeddings, np.array(ids))
        logging.debug(f"Fragmentos agregados a FAISS con IDs: {ids}")
        logging.debug(f"Total de fragmentos indexados: {index.ntotal}")
    except Exception as e:
        logging.error(f"Error al agregar fragmentos al índice FAISS: {e}")

# Función para buscar fragmentos relevantes
def buscar_fragmentos(index, query, k=5):
    try:
        embedding_query = model.encode([query])
        embedding_query = np.array([embedding_query / np.linalg.norm(embedding_query)])
        logging.debug(f"Embedding de la consulta: {embedding_query}")
        
        # Realizar la búsqueda de los fragmentos más cercanos
        result = index.search(embedding_query, k)
        logging.debug(f"Resultado bruto de FAISS: {result}")

        if isinstance(result, tuple) and len(result) == 2:
            D, I = result
            logging.debug(f"Distancias: {D}, IDs: {I}")

            if I is None or len(I) == 0:
                logging.debug("No se encontraron fragmentos relevantes.")
                return None, None

            return I[0], D[0]
        else:
            logging.error(f"FAISS devolvió un resultado inesperado: {result}")
            return None, None
    except Exception as e:
        logging.error(f"Error en la búsqueda de fragmentos en FAISS: {e}")
        return None, None
