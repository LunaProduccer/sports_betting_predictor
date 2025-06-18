# backend/app.py (Versión Final con Modelo Integrado)
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# --- CARGA DEL MODELO ENTRENADO ---
try:
    model = joblib.load('models/random_forest_model.joblib')
    # Define las columnas en el orden exacto que tu modelo espera
    model_columns = [
        'tiros_local', 'tiros_visitante', 'tiros_apuerta_local', 'tiros_apuerta_visitante',
        'posesion_local', 'posesion_visitante', 'corners_local', 'corners_visitante'
        # Asegúrate que estas columnas coincidan con las que usaste en Colab
    ]
    print("* Modelo de ML cargado exitosamente.")
except Exception as e:
    model = None
    print(f"* Error al cargar el modelo: {e}")

@app.route('/')
def home():
    return "API del Backend Predictivo ¡Funcionando con un modelo real!"

@app.route('/api/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "El modelo de ML no está cargado."}), 500
    try:
        data = request.get_json()
        # Crea un DataFrame para asegurar el orden de las columnas
        input_df = pd.DataFrame([data])
        final_df = input_df[model_columns]

        # Hacer la predicción
        prediction_raw = model.predict(final_df)
        probabilities_raw = model.predict_proba(final_df)

        # Mapear resultado numérico a texto
        resultado_map = {2: 'GANA LOCAL', 1: 'EMPATE', 0: 'GANA VISITANTE'}
        predicted_class_text = resultado_map.get(prediction_raw[0], 'Desconocido')
        max_probability = float(np.max(probabilities_raw))

        response = {
            "result": predicted_class_text,
            "probability": max_probability
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error interno: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)