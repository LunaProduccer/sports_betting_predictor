# backend/recolector_de_datos.py (Versión Inteligente)

import requests
import csv
import time
import os # Importamos 'os' para revisar si un archivo existe

# --- CONFIGURACIÓN ---
API_KEY = "3662c82bee725cc73567b4594fa88001"
API_HOST = "v3.football.api-sports.io"
HEADERS = {'x-rapidapi-host': API_HOST, 'x-rapidapi-key': API_KEY}

LEAGUE_ID = 140
SEASON = 2023
CSV_FILENAME = f"datos_liga_{LEAGUE_ID}_temporada_{SEASON}.csv"

def obtener_partidos_de_liga(league_id, season):
    # ... (Esta función se queda igual que antes)
    url = f"https://{API_HOST}/fixtures"
    params = {'league': league_id, 'season': season}
    print(f"Obteniendo partidos para la liga {league_id}, temporada {season}...")
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Se encontraron {data['results']} partidos.")
        return data['response']
    except Exception as e:
        print(f"Error obteniendo partidos: {e}")
        return []

def obtener_estadisticas_partido(fixture_id):
    # ... (Esta función también se queda igual)
    url = f"https://{API_HOST}/fixtures/statistics"
    params = {'fixture': fixture_id}
    time.sleep(1.2) # Aumentamos un poco la pausa para ser más seguros con la API
    print(f"Obteniendo estadísticas para el partido ID: {fixture_id}")
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        return data['response']
    except Exception as e:
        print(f"Error obteniendo estadísticas para el partido {fixture_id}: {e}")
        return []

# --- SCRIPT PRINCIPAL (La Lógica Mejorada) ---
if __name__ == "__main__":
    partidos = obtener_partidos_de_liga(LEAGUE_ID, SEASON)
    
    partidos_ya_descargados = set()
    
    # 1. REVISAMOS SI EL ARCHIVO YA EXISTE
    if os.path.exists(CSV_FILENAME):
        print(f"El archivo '{CSV_FILENAME}' ya existe. Leyendo partidos ya descargados...")
        with open(CSV_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                partidos_ya_descargados.add(int(row['partido_id']))
        print(f"Se encontraron {len(partidos_ya_descargados)} partidos ya procesados. Se continuará desde ahí.")

    # 2. ABRIMOS EL ARCHIVO EN MODO 'APPEND' ('a') o 'WRITE' ('w')
    # Si el archivo no existía, se crea con 'w'. Si ya existía, se abre con 'a' para añadir al final.
    modo_apertura = 'a' if os.path.exists(CSV_FILENAME) else 'w'
    
    with open(CSV_FILENAME, mode=modo_apertura, newline='', encoding='utf-8') as csv_file:
        fieldnames = [
            'partido_id', 'resultado_final_local', 'resultado_final_visitante',
            'tiros_local', 'tiros_visitante', 'tiros_apuerta_local', 'tiros_apuerta_visitante',
            'posesion_local', 'posesion_visitante', 'corners_local', 'corners_visitante'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Si estamos creando el archivo por primera vez (modo 'w'), escribimos el encabezado
        if modo_apertura == 'w':
            writer.writeheader()

        if partidos:
            for partido in partidos:
                fixture_id = partido['fixture']['id']

                # 3. SALTAMOS LOS PARTIDOS QUE YA TENEMOS
                if fixture_id in partidos_ya_descargados:
                    print(f"Saltando partido ID {fixture_id}, ya está en el CSV.")
                    continue

                estadisticas = obtener_estadisticas_partido(fixture_id)

                if len(estadisticas) == 2:
                    # ... (El resto de la lógica para extraer y escribir la fila es la misma)
                    # ... (código omitido por brevedad, es igual al que ya tenías)
                    local_stats = estadisticas[0]['statistics']
                    visitante_stats = estadisticas[1]['statistics']
                    def get_stat(stats, stat_name): # Función auxiliar
                        for stat in stats:
                            if stat['type'] == stat_name: return stat['value'] if stat['value'] is not None else 0
                        return 0
                    fila = {
                        'partido_id': fixture_id,
                        'resultado_final_local': partido['goals']['home'],
                        'resultado_final_visitante': partido['goals']['away'],
                        'tiros_local': get_stat(local_stats, 'Total Shots'),
                        'tiros_visitante': get_stat(visitante_stats, 'Total Shots'),
                        'tiros_apuerta_local': get_stat(local_stats, 'Shots on Goal'),
                        'tiros_apuerta_visitante': get_stat(visitante_stats, 'Shots on Goal'),
                        'posesion_local': str(get_stat(local_stats, 'Ball Possession')).replace('%', ''),
                        'posesion_visitante': str(get_stat(visitante_stats, 'Ball Possession')).replace('%', ''),
                        'corners_local': get_stat(local_stats, 'Corner Kicks'),
                        'corners_visitante': get_stat(visitante_stats, 'Corner Kicks'),
                    }
                    writer.writerow(fila)
                    partidos_ya_descargados.add(fixture_id) # Actualizamos nuestro registro de procesados

    print(f"\n¡Proceso completado! Total de partidos en el archivo: {len(partidos_ya_descargados)}")