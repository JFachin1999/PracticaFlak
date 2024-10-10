from flask import Flask, jsonify
from Webscraping import programa  # Asegúrate de que el módulo exista y tenga la función 'programa'
import pandas as pd

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def home():
    resultado = programa()  # Llamamos a la función 'programa()' que devuelve un DataFrame
    return resultado.to_json()  # Convertimos el DataFrame a JSON y lo devolvemos como respuesta

# Verifica si este archivo se está ejecutando directamente y lanza el servidor
if __name__ == '__main__':
    app.run(debug=True)
