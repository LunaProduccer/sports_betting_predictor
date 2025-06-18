# backend/test_api.py (para depurar el problema de los partidos)
import requests
import json

API_KEY = "3662c82bee725cc73567b4594fa88001" # Reemplaza con tu clave
API_HOST = "v3.football.api-sports.io"
HEADERS = {'x-rapidapi-host': API_HOST, 'x-rapidapi-key': API_KEY}

# Esta es la petición exacta que está fallando en tu recolector
url = f"https://{API_HOST}/fixtures"
params = {'league': 140, 'season': 2023} 

print("Haciendo la petición de depuración al endpoint /fixtures...")

try:
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    print("\n--- RESPUESTA COMPLETA DE LA API ---")
    print(json.dumps(data, indent=4))

except Exception as e:
    print(f"Ocurrió un error: {e}")