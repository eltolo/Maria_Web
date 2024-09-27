import json
import os

def load_chat_history(history_file):
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
                return history[-10:]
        except json.JSONDecodeError:
            print("El archivo de historial está vacío o corrupto. Se iniciará un nuevo historial.")
            return []
    return []

def save_chat_history(history_file, chat_history):
    try:
        # Convertir todo el contenido a string para evitar errores de serialización
        for message in chat_history:
            message["content"] = str(message["content"])
        
        # Guardar el historial en formato JSON
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(chat_history, f, ensure_ascii=False, indent=4)
    except TypeError as e:
        print(f"Error al guardar el historial de chat: {e}")

