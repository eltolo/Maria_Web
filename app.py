from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os, sys
import docx
import openai

from dotenv import load_dotenv
# Cargar las variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY no encontrado en las variables de entorno.")
    sys.exit(1)

# Configurar la clave API de OpenAI
openai.api_key = OPENAI_API_KEY

# Ruta del directorio actual y añadir al sys.path
project_path = os.getcwd()  
print(f"path: {project_path}")
sys.path.append(project_path)

from modulo_fragmenter.fragmenter import dividir_en_fragmentos
from modulo_faiss.faiss_index import crear_indice_faiss
from modulo_db.db_manager import conectar_db, insertar_documento_y_fragmentos
from modulo_llm.llm_manager import get_llm, send_query_to_ollama  # Importamos el modelo y la función para procesar el texto

app = Flask(__name__)
app.secret_key = '20clave24'  # Establece una clave secreta
# Inicializar FAISS y la base de datos
faiss_index = crear_indice_faiss(dimension_embedding=384)  # Ajusta el tamaño del embedding según tu modelo
conn = conectar_db()

# Ruta raíz para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para subir el documento .docx
@app.route('/upload_document', methods=['POST'])
def upload_document():
    file = request.files['file']
    
    if file and file.filename.endswith('.docx'):
        document = docx.Document(file)
        texto = "\n".join([para.text for para in document.paragraphs])  # Leer el contenido del archivo .docx
        
        # Nombre del documento
        nombre_documento = file.filename

        # Insertar el documento y fragmentos en la base de datos e indexarlos en FAISS
        document_id = insertar_documento_y_fragmentos(conn, nombre_documento, texto, faiss_index)
        
        if document_id:
            flash("Documento cargado e indexado correctamente")
        else:
            flash("Hubo un error al cargar el documento")

        return redirect(url_for('index'))
    else:
        flash("Solo se permiten archivos .docx")
        return redirect(url_for('index'))

# Nueva ruta para manejar el envío de texto por AJAX y procesar con el modelo LLM
@app.route('/send_text_ajax', methods=['POST'])
def send_text_ajax():
    data = request.get_json()  # Obtener datos enviados vía AJAX
    input_text = data.get('input_text')

    if input_text:
        # Obtener el modelo y su tipo (OpenAI o Llama)
        llm, tipo_modelo = get_llm()

        if llm:
            # Usar el modelo para procesar el texto
            chat_history = []  # Puedes agregar lógica de historial de chat si lo necesitas
            response = send_query_to_ollama("", llm, tipo_modelo, input_text, chat_history, None)

            return jsonify({'output': response})  # Enviar el texto procesado como respuesta
        else:
            return jsonify({'error': 'No se pudo cargar el modelo'}), 500
    else:
        return jsonify({'error': 'No se envió ningún texto'}), 400

# Ruta para mostrar la página de reconocimiento de voz
@app.route('/reconocimiento')
def reconocimiento():
    return render_template('reconocimiento.html')

# Iniciar la aplicación web
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
