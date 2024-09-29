from openai import OpenAI

from dotenv import load_dotenv
# Cargar las variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY no encontrado en las variables de entorno.")
    sys.exit(1)
# Configurar la clave API de OpenAI
openai.api_key = OPENAI_API_KEY


# Instancia del cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


print (generate_response("donde queda Paso de los Libres en Argentina?"))


