# modulo: test_db_manager.py
import os
from modulo_db.db_manager import conectar_db, crear_tablas, insertar_documento, insertar_fragmento, obtener_fragmentos

def test_db_operations():
    # Conectar a la base de datos
    conn = conectar_db("test_maria_knowledge.db")
    if conn:
        print("Conexión a la base de datos establecida.")
    
        # Crear las tablas
        crear_tablas(conn)
        print("Tablas creadas con éxito.")
        
        # Insertar un documento
        document_id = insertar_documento(conn, "Documento de Prueba")
        if document_id:
            print(f"Documento insertado con éxito. ID: {document_id}")
        
        # Insertar fragmentos del documento
        fragmento_1 = "Este es el primer fragmento del documento."
        fragmento_2 = "Este es el segundo fragmento del documento."
        insertar_fragmento(conn, document_id, fragmento_1, 1)
        insertar_fragmento(conn, document_id, fragmento_2, 2)
        print("Fragmentos insertados con éxito.")
        
        # Consultar fragmentos
        fragmentos = obtener_fragmentos(conn, document_id)
        if fragmentos:
            print("Fragmentos obtenidos con éxito:")
            for fragmento in fragmentos:
                print(fragmento[0])  # El texto de cada fragmento
        
        # Cerrar la conexión
        conn.close()
        print("Conexión cerrada.")
    else:
        print("Error al conectar a la base de datos.")

if __name__ == "__main__":
    test_db_operations()

