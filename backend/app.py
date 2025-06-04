from flask import Flask, request, jsonify
from flask_cors import CORS
# import joblib # Lo usaremos en breve, cuando integremos el modelo
# import numpy as np # También para el modelo

app = Flask(__name__)
CORS(app) # Esto habilita CORS para todas las rutas y orígenes.

# Aquí es donde cargaremos nuestro modelo de Machine Learning más adelante
# model = None 
# print("* Modelo aún no cargado")

@app.route('/')
def home():
    return "¡API del Backend para Predicciones Deportivas Funcionando!"

# Este será nuestro endpoint para las predicciones. Lo construiremos paso a paso.
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Aquí irá la lógica para:
#     # 1. Recibir los datos del frontend.
#     # 2. Preparar los datos para el modelo.
#     # 3. Usar el modelo para hacer una predicción.
#     # 4. Devolver la predicción al frontend.
#     data = request.get_json()
#     # ... más lógica aquí ...
#     return jsonify({"message": "Endpoint de predicción listo para implementar", "received_data": data})

if __name__ == '__main__':
    # Cuando ejecutes "python app.py", esto iniciará el servidor de desarrollo de Flask.
    # debug=True es útil para desarrollo porque recarga el servidor con los cambios y muestra errores detallados.
    # port=5000 es el puerto estándar para Flask, pero puedes cambiarlo si es necesario.
    app.run(debug=True, port=5000)