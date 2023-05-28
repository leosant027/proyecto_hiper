from costante_gral import URL_BASE
from funciones.api import consumir_api
from funciones.parses import parse_categoria
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
        categorias.append(parse_categoria(category_data))

    categorias_y_subcategorias = []

    # Aquí es donde agregamos el indicador de progreso
    for categoria in tqdm(categorias, desc='Processing categories'):
        categoria_dict = {
            "nombre": categoria.name,
            "id": categoria.id,
            "url": categoria.url,
            "cantidad_productos": 0,
            "subcategorias": [],
            "marcas": []
        }

        urlinfo = f"{URL_BASE}/api/catalog_system/pub/facets/search{categoria.url}/?map=c"
        data_info = consumir_api(urlinfo, headers)

        # Agregar cantidad de productos y marcas
        categoria_dict["cantidad_productos"] = data_info['CategoriesTrees'][0]['Quantity']
        for marca in data_info['Brands']:
            marca_dict = {
                "id": 0,
                "nombre": marca['Name'],
            }
            categoria_dict["marcas"].append(marca_dict)

        # Agregar subcategorias y sus datos
        for subcategoria in categoria.children:
            subcategoria_dict = {
                "id": subcategoria.id,
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
