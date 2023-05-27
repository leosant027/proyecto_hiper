import json
def seleccionar_opcion(archivo_json, atributo):
    # Abre el archivo json y lee los datos
    with open(archivo_json, 'r') as f:
        data = json.load(f)

    # Extrae las opciones del archivo json
    options = data[atributo]

    # Imprime las opciones y solicita al usuario que elija una
    for i, option in enumerate(options, 1):
        print(f"{i}. {option['nombre']}")

    choice = int(input("Elige una opción (introduce el número correspondiente): "))

    # Asegúrate de que la opción elegida sea válida
    if 1 <= choice <= len(options):
        chosen_option = options[choice - 1]
        print(chosen_option)
        return chosen_option
    else:
        print("Elección inválida, intenta de nuevo.")
        return None
