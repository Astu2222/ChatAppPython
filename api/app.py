from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials

# clave dani: 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
# clave nahue : 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

# 2jP3asBGFrtlIkef5RcNT3BlbkFJ6rlNdOtizErS6txYzIXe

openai.api_key = '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'

# Mensaje inicial del chat
initial_message = "Bienvenido a TigerIA, en qué te puedo ayudar?"

# Define la default route para cargar el archivo index.html
@app.route("/")
def index():
    return render_template("index.html")

# Define la ruta /api para manejar las solicitudes POST
@app.route("/api", methods=["POST"])
def api():
    # Obtiene el mensaje de la solicitud POST
    user_message = request.json.get("message")

    # Obtiene la URL actual
    current_url = request.referrer

    # Define el contexto general (deporte y salud)
    context = "Deporte y Salud:"

    # Verifica si la URL actual corresponde a tu sitio web
    if "http://grupo3frontv2.s3-website.us-east-2.amazonaws.com/" in current_url:
        context = "Productos de artículos deportivos para rentar:"

    # Agrega el mensaje inicial y el contexto al lado del chat
    messages = [
        {"role": "system", "content": "system:other"},
        {"role": "user", "content": f"{context} {initial_message}"},
        {"role": "user", "content": user_message}
    ]

    # Envía el mensaje a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Obtiene la respuesta del modelo
    bot_message = response.choices[0].message.get("content", "No se generó una respuesta")

    # Devuelve la respuesta del bot como JSON
    return jsonify({"message": bot_message})

if __name__ == '__main__':
    app.run()
