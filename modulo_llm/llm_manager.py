# modulo: llm_manager.py
import requests, os
from openai import OpenAI
from modulo_config.config import cargar_configuracion
# Librerias Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv
# Cargar las variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY no encontrado en las variables de entorno.")
    sys.exit(1)

print(api:OPENAI_API_KEY)
# Instanciar el cliente de OpenAI para gpt-3.5-turbo

client = OpenAI(api_key=OPENAI_API_KEY)

class OpenAILLM:
    def __init__(self, model="gpt-3.5-turbo", temperature=0.2, max_tokens=1500):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    def generate(self, prompt):
        try:
            # Usar el método correcto 'chat.completions.create'
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            print("\nOpenAILLM - response: ",response.choices[0].message.content.strip())
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error con OpenAI: {str(e)}")
            return None


def obtener_servidor_activo(servidores):
    """
    Detecta qué servidor Ollama está activo.
    """
    for servidor in servidores:
        try:
            response = requests.get(f"{servidor['base_url']}")  #/status
            if response.status_code == 200:
                return servidor
        except Exception:
            continue
    return None

def get_llm(config_file="Maria.yaml"):
    """
    Devuelve la instancia del modelo junto con el tipo ('llama3' o 'OpenAI').
    También se carga la configuración desde el archivo YAML.
    """
    try:
        config = cargar_configuracion(config_file)

        temperature = config['OpenAI']['temperatura']
        max_tokens = config['OpenAI']['max_tokens']

        servidores = config['llama3']['servidores']

        servidor_activo = obtener_servidor_activo(servidores)

        if servidor_activo:
            return ChatOllama(model=servidor_activo["model"], base_url=servidor_activo["base_url"], temperature=temperature), "llama3"
        else:
            return OpenAILLM(temperature=temperature, max_tokens=max_tokens), "OpenAI"
    
    except Exception as e:
        print(f"get_llm - Error cargando la configuración: {e}")
        return None, None
        
        
        
def send_query_to_ollama(prompt, llm, tipo_modelo, user_input, chat_history, history_file):
    """
    Envía el prompt, el historial y el input del usuario al modelo adecuado y maneja errores detalladamente.
    """
    try:
        # Construir el historial del chat en formato de texto
        recent_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])

        if tipo_modelo == "llama3":
            formatted_prompt = prompt.format(context=recent_history, input=user_input)
            respuesta_ollama = llm.invoke(formatted_prompt)
            response = respuesta_ollama.content
        elif tipo_modelo == "OpenAI":
            response = llm.generate(user_input)

        print("send_query_to_ollama - response:", response)
        return response

    except ValueError as ve:
        error_msg = f"Error de valor en {tipo_modelo}: {ve}"
        print(error_msg)
        return f"Error procesando la consulta: {ve}. Verifica el formato de los datos."

    except ConnectionError as ce:
        error_msg = f"Error de conexión al servidor {tipo_modelo}: {ce}"
        print(error_msg)
        return f"Error procesando la consulta: {ce}. Verifica la conectividad con el servidor."

    except Exception as e:
        error_msg = f"Error general con {tipo_modelo}: {e}"
        print(error_msg)
        return f"Error procesando la consulta: {e}. Revisa los logs para más detalles."






