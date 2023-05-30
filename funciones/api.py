import time

import requests

from costante_gral import MAX_REINTENTOS


def consumir_api(url, headers):
    """
    Esta función envía una solicitud GET a una URL y devuelve la respuesta en formato JSON.

    Parámetros:
    url (str): La URL a la que se enviará la solicitud GET.
    headers (dict): Un diccionario que contiene los encabezados HTTP de la solicitud.
    max_reintentos (int, opcional): El número máximo de intentos que se harán si la solicitud falla. Por defecto es 2.

    Retorna:
    dict: La respuesta de la solicitud en formato JSON.

    Lanza:
    SystemExit: Si la solicitud falla después de max_reintentos, se lanza una excepción de tipo SystemExit.
    """
    max_reintentos = MAX_REINTENTOS
    for i in range(max_reintentos):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de estado HTTP 4XX o 5XX
            return response.json()
        except requests.exceptions.RequestException as e:
            if i < max_reintentos - 1:  # si no es el último intento
                time.sleep(5 * (i + 1))  # esperar 5 segundos en el primer intento, 10 en el segundo, etc.
                continue
            else:  # si es el último intento, lanzar la excepción
                raise SystemExit(e)
