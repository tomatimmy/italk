from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from gpt4all import GPT4All

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Cargar modelo de GPT4All
model = GPT4All("mistral-7b-instruct")  # Asegúrate de tener el modelo descargado

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("iniciar_conversacion")
def iniciar_conversacion():
    mensaje = "Hola, ¿cómo estás?"
    respuesta = generar_respuesta(mensaje)
    emit("mensaje", {"nombre": "IA_1", "texto": mensaje})
    socketio.sleep(1)
    emit("mensaje", {"nombre": "IA_2", "texto": respuesta})
    continuar_conversacion(respuesta)

def continuar_conversacion(mensaje_anterior):
    while True:
        respuesta = generar_respuesta(mensaje_anterior)
        emit("mensaje", {"nombre": "IA_1", "texto": respuesta}, broadcast=True)
        socketio.sleep(2)
        
        nueva_respuesta = generar_respuesta(respuesta)
        emit("mensaje", {"nombre": "IA_2", "texto": nueva_respuesta}, broadcast=True)
        socketio.sleep(2)
        
        mensaje_anterior = nueva_respuesta

def generar_respuesta(mensaje):
    return model.generate(mensaje)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
