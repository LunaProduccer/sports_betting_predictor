# backend/buscar_ligas.py

import requests
import json

# --- ¡Pega tu API Key aquí! ---
API_KEY = "3662c82bee725cc73567b4594fa88001"
API_HOST = "v3.football.api-sports.io"
HEADERS = {'x-rapidapi-host': API_HOST, 'x-rapidapi-key': API_KEY}

# El endpoint para buscar ligas
url = f"https://{API_HOST}/leagues"

# Pedimos al usuario que escriba el nombre de un país en inglés
pais_buscado = input("Escribe el nombre de un país en inglés (ej: Spain, England, Peru, Italy, Germany): ")

# Preparamos los parámetros para la búsqueda
params = {'country': pais_buscado}

try:
    print(f"\nBuscando ligas para '{pais_buscado}'...")
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    if data['results'] > 0:
        print(f"\n--- Ligas encontradas para '{pais_buscado}' ---")
        for item in data['response']:
            league_info = item['league']
            country_info = item['country']
            print(f"  - Nombre: {league_info['name']} | ID: {league_info['id']} | País: {country_info['name']}")
        print("-----------------------------------------")
    else:
        print(f"No se encontraron ligas para el país '{pais_buscado}'. Revisa que esté bien escrito en inglés.")

except Exception as e:
    print(f"Ocurrió un error: {e}")