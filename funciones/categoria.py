from costante_gral import URL_BASE, MAX_PRODUCTOS_POR_PAGINA, RUTA_DATOS
from funciones.api import consumir_api
from funciones.json_funciones import leer_json, guardar_json
from funciones.parses import parse_categorias
import json
from tqdm import tqdm


def listar_categoria(headers):
    """
    Esta función lista las categorías obtenidas de una API,
    parsea los datos, y los guarda en un archivo JSON.

    Parámetros:
    headers (dict): Un diccionario que contiene los encabezados HTTP de la solicitud.

    El archivo 'categorias.json' se guardará en el directorio 'data'.
    """
    url = f"{URL_BASE}/api/catalog_system/pub/category/tree/50"
    data = consumir_api(url, headers)
    categorias = []

    # Parsear los datos de las categorías
    for category_data in data:
        categorias.append(parse_categorias(category_data))

    categorias_y_subcategorias = []

    # Aquí es donde agregamos el indicador de progreso
    for categoria in tqdm(categorias, desc='Procesando categorias'):
        categoria_dict = {
            "nombre": categoria.name,
            "categoria_id": categoria.category_id,
            "url": categoria.url,
            "cantidad_productos": 0,
            "subcategorias": [],
            "marcas": [],
            "paginas": []
        }

        urlinfo = f"{URL_BASE}/api/catalog_system/pub/facets/search{categoria.url}/?map=c"
        data_info = consumir_api(urlinfo, headers)

        # Agregar cantidad de productos y marcas
        cantidad_productos = data_info['CategoriesTrees'][0]['Quantity']
        categoria_dict["cantidad_productos"] = cantidad_productos
        # Creando paginacion
        total_paginas = (cantidad_productos - 1) // MAX_PRODUCTOS_POR_PAGINA + 1
        for pagina in range(total_paginas):
            inicio = pagina * MAX_PRODUCTOS_POR_PAGINA
            fin = inicio + MAX_PRODUCTOS_POR_PAGINA
            pagina_dict = {
                "pagina": pagina + 1,
                "url": f"_from={inicio}&_to={fin}"
            }
            categoria_dict["paginas"].append(pagina_dict)
        for marca in data_info['Brands']:
            marca_dict = {
                "id": 0,
                "nombre": marca['Name'],
            }
            categoria_dict["marcas"].append(marca_dict)

        # Agregar subcategorias y sus datos
        for subcategoria in categoria.children:
            subcategoria_dict = {
                "categoria_id": subcategoria.category_id,
                "nombre": subcategoria.name,
                "url": subcategoria.url,
                "cantidad_productos": 0,
            }
            categoria_dict["subcategorias"].append(subcategoria_dict)

            urlinfosubcat = f"{URL_BASE}/api/catalog_system/pub/facets/search{subcategoria.url}/?map=c,c"
            data_infosubcat = consumir_api(urlinfosubcat, headers)
            subcategoria_dict["cantidad_productos"] = data_infosubcat['CategoriesTrees'][0]['Quantity']

        categorias_y_subcategorias.append(categoria_dict)

    # Guardar los datos parseados en un archivo JSON
    with open('data/categorias.json', 'w', encoding='utf-8') as f:
        json.dump(categorias_y_subcategorias, f, ensure_ascii=False, indent=4)


def mapear_categorias():
    # Leer archivo
    data = leer_json(f'{RUTA_DATOS}categorias.json')
    # Crear un nuevo JSON
    nuevo_json = []

    # Procesar cada elemento en el JSON proporcionado
    for item in data:
        # Añadir la categoría principal
        nuevo_json.append({
            "id": item["categoria_id"],
            "nombre": item["nombre"]
        })

        # Añadir cada subcategoría
        for subcategoria in item.get("subcategorias", []):
            nuevo_json.append({
                "id": subcategoria["categoria_id"],
                "nombre": subcategoria["nombre"]
            })

    # Ordenar la lista resultante por id
    nuevo_json = sorted(nuevo_json, key=lambda x: x['id'])
    guardar_json(nuevo_json, f'{RUTA_DATOS}lista_categoria.json')
