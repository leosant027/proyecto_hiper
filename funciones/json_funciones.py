import json


def crear_menu(data, atributo=None, key_menu="nombre"):
    """
    Esta función presenta una lista de opciones al usuario y le permite seleccionar una.

    Parámetros: data (str/dict): El camino al archivo JSON que contiene las opciones o un diccionario de Python.
    atributo (str, opcional): El atributo en el JSON que contiene las opciones. Si no se proporciona o si el atributo
    no existe, se utilizan todos los datos en el archivo JSON. key_menu (str, opcional): La clave que se debe
    utilizar para mostrar las opciones al usuario. Por defecto es "nombre".

    Retorna:
    dict: La opción seleccionada por el usuario. Si el usuario selecciona una opción inválida, la función retorna None.
    """
    # Si data es una cadena, se supone que es una ruta a un archivo y se intenta cargar
    if isinstance(data, str):
        with open(data, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # Intenta extraer las opciones del archivo json
    if atributo is None:
        options = data
    else:
        options = data[atributo]

    while True:
        # Imprime las opciones y solicita al usuario que elija una
        for i, option in enumerate(options, 1):
            print(f"{i}. {option[key_menu]}")

        choice = int(input("Elige una opción (introduce el número correspondiente): "))

        # Asegúrate de que la opción elegida sea válida
        if 1 <= choice <= len(options):
            chosen_option = options[choice - 1]
            return chosen_option
        else:
            print("Elección inválida, intenta de nuevo.")


def leer_json(archivo):
    with open(archivo, encoding='utf-8') as file:
        data = json.load(file)
    return data


def guardar_json(data, archivo):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
