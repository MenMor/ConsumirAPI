import requests

def get_top_headlines(api_key):
    # Endpoint para obtener los titulares principales
    url = 'https://newsapi.org/v2/top-headlines'
    # Parámetros para la solicitud
    params = {
        'country': 'us',  # Noticias de Estados Unidos
        'apiKey': api_key
    }
    # Realizar la petición GET
    response = requests.get(url, params=params)
    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        return response.json()  # Devuelve la respuesta en formato JSON
    else:
        return response.status_code, response.text  # Devuelve código de error y mensaje

# Usar la función con tu API key
api_key = 'c3cfd796413549958827db61bf0dd3d9'
news_data = get_top_headlines(api_key)
print(news_data)
