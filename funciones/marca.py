from costante_gral import RUTA_DATOS
from funciones.json_funciones import leer_json, guardar_json


def mapear_marcas():
    # Leer archivo
    archivo = leer_json(f'{RUTA_DATOS}categorias.json')
    # Crear un nuevo JSON
    nuevo_json = []

    # Procesar cada elemento en el JSON proporcionado
    for item in archivo:
        # Añadir cada marca
        for marca in item.get("marcas", []):
            nuevo_json.append({
                "id": marca["id"],
                "nombre": marca["nombre"]
            })

    # Ordenar la lista resultante por id
    nuevo_json = sorted(nuevo_json, key=lambda x: x['id'])
    guardar_json(nuevo_json, f'{RUTA_DATOS}listado_marca.json')


def actualizar_marcas():
    # Archivo JSON original
    archivo_original = f'{RUTA_DATOS}categorias.json'

    # Archivo JSON para reemplazar los valores de "id"
    archivo_reemplazo = f'{RUTA_DATOS}lista_marcas.json'

    # Cargar los JSON como diccionarios
    json_data = leer_json(archivo_original)
    json_reemplazo = leer_json(archivo_reemplazo)

    # Reemplazar los valores de "id" en el JSON original
    for item in json_data[0]["marcas"]:
        if item["id"] == 0:
            item["id"] = next((marca["id"] for marca in json_reemplazo if marca["nombre"] == item["nombre"]), 0)

    # Guardar el JSON actualizado en un archivo
    archivo_actualizado = f'{RUTA_DATOS}categorias_completa.json'
    guardar_json(json_data, archivo_actualizado)
