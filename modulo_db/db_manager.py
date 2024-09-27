# módulo: db_manager.py
import sqlite3
import logging
from datetime import datetime
from modulo_fragmenter.fragmenter import dividir_en_fragmentos
from modulo_faiss.faiss_index import agregar_fragmentos_a_faiss

# Configuración del logging para capturar errores
log_file = "db_errors.log"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Función para conectar a la base de datos SQLite
def conectar_db(db_name="maria_knowledge.db"):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error al conectar a la base de datos: {e}")
        return None

# Función para crear las tablas documentos y fragmentos
def crear_tablas(conn):
    try:
        cursor = conn.cursor()

        # Crear tabla de documentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha_carga TEXT NOT NULL
            )
        ''')

        # Crear tabla de fragmentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fragmentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id INTEGER NOT NULL,
                texto TEXT NOT NULL,
                orden INTEGER NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documentos (id)
            )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al crear tablas: {e}")

# Función para insertar un nuevo documento y fragmentarlo
def insertar_documento_y_fragmentos(conn, nombre, texto, faiss_index):
    try:
        cursor = conn.cursor()
        fecha_carga = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO documentos (nombre, fecha_carga)
            VALUES (?, ?)
        ''', (nombre, fecha_carga))
        conn.commit()
        document_id = cursor.lastrowid  # ID del documento insertado

        # Fragmentar el documento
        fragmentos = dividir_en_fragmentos(texto, max_palabras=128)
        ids = []
        print(f"Fragmentos generados: {fragmentos}")

        for i, fragmento in enumerate(fragmentos):
            cursor.execute('''
                INSERT INTO fragmentos (document_id, texto, orden)
                VALUES (?, ?, ?)
            ''', (document_id, fragmento, i))
            ids.append(cursor.lastrowid)  # Guardar los IDs de los fragmentos insertados

        conn.commit()

        # Agregar fragmentos a FAISS
        agregar_fragmentos_a_faiss(faiss_index, fragmentos, ids)

        return document_id
    except sqlite3.Error as e:
        logging.error(f"Error al insertar documento y fragmentos: {e}")
        return None

# Función para consultar fragmentos de un documento por ID
def obtener_fragmentos(conn, document_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT texto FROM fragmentos
            WHERE document_id = ?
            ORDER BY orden ASC
        ''', (document_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error al obtener fragmentos: {e}")
        return None
