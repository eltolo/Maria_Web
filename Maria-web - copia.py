from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os ,sys


# Ruta del directorio actual y añadir al sys.path
project_path = os.getcwd()  
print(f"path: {project_path}")
sys.path.append(project_path)

# Ruta del directorio actual y añadir al sys.path
project_path = os.getcwd()  
print(f"path: {project_path}")
sys.path.append(project_path)



from modulo_fragmenter.fragmenter import dividir_en_fragmentos
from modulo_faiss.faiss_index import crear_indice_faiss
from modulo_db.db_manager import conectar_db, insertar_documento_y_fragmentos
import docx

app = Flask(__name__)

# Inicializar FAISS y la base de datos
faiss_index = crear_indice_faiss(dimension_embedding=384)  # Ajusta el tamaño del embedding según tu modelo
conn = conectar_db()

# Ruta para subir el documento
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

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Iniciar la aplicación web
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
