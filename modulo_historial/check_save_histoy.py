import json


historia = [{'role': 'human', 'content': 'Hols'}, {'role': 'assistant', 'content': 'Hola, ¿cómo estás? ¿En qué puedo ayudarte hoy?'}, {'role': 'human', 'content': 'todo bien vos?'}, {'role': 'assistant', 'content': '¡Hola! Sí, estoy bien, ¿cómo estás tú? ¿En qué puedo ayudarte hoy?'}, {'role': 'human', 'content': 'Me llamo Jorge y tu?'}, {'role': 'assistant', 'content': 'Hola Jorge, soy un asistente virtual y no tengo un nombre como los humanos. ¿En qué puedo ayudarte hoy?'}, {'role': 'human', 'content': 'Bueno para dirijirme a ti, te llamare Maria, puede ser?'}, {'role': 'assistant', 'content': 'Claro, puedes llamarme Maria. ¿En qué puedo ayudarte?'}]
history_file = "maria_history.json"

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

save_chat_history(history_file, historia)