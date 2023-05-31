import time
import requests

from costante_gral import MAX_REINTENTOS


def consumir_api(url: str, headers: dict, proxy: str = None) -> dict:
    """
    Esta función envía una solicitud GET a una URL y devuelve la respuesta en formato JSON.

    Parámetros:
    - url (str): La URL a la que se enviará la solicitud GET.
    - headers (dict): Un diccionario que contiene los encabezados HTTP de la solicitud.
    - proxy (str, opcional): La dirección del proxy a utilizar. Por defecto es None.

    Retorna:
    - dict: La respuesta de la solicitud en formato JSON.

    Lanza:
    - SystemExit: Si la solicitud falla después de max_reintentos, se lanza una excepción de tipo SystemExit.
    """

    max_reintentos = MAX_REINTENTOS
    for i in range(max_reintentos):
        try:
            if proxy:
                proxies = {
                    'http': proxy,
                    'https': proxy
                }
                response = requests.get(url, headers=headers, proxies=proxies)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de estado HTTP 4XX o 5XX
            return response.json()
        except requests.exceptions.RequestException as e:
            if i < max_reintentos - 1:  # si no es el último intento
                time.sleep(5 * (i + 1))  # esperar 5 segundos en el primer intento, 10 en el segundo, etc.
                continue
            else:  # si es el último intento, lanzar la excepción
                raise SystemExit(e)
