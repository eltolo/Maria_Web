from openai import OpenAI
OPENAI_API_KEY="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"
# Instancia del cliente de OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


print (generate_response("donde queda Paso de los Libres en Argentina?"))


