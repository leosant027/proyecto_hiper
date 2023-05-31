from costante_gral import URL_BASE, MAX_PRODUCTOS_POR_PAGINA, RUTA_DATOS
from funciones.api import consumir_api
from funciones.csv_funciones import leer_csv, actualizar_valores, obtener_valor
from funciones.json_funciones import leer_json, guardar_json
from funciones.parses import parse_categoria_temp
import json
from tqdm import tqdm

from modelos.categoria_temp import CategoriaTemp


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
    categorias_y_subcategorias = []

    # Parsear los datos de las categorías
    for category_data in data:
        categorias.append(parse_categoria_temp(category_data))
    for categoria in categorias:
        urlinfo = f"{URL_BASE}/api/catalog_system/pub/facets/search{categoria.url}/?map=c"
        data_info = consumir_api(urlinfo, headers)
        paginas = []
        marcas = []
        cantidad_productos = data_info['CategoriesTrees'][0]['Quantity']
        categoria.cantidad_productos = cantidad_productos
        # Creando paginacion
        total_paginas = (cantidad_productos - 1) // MAX_PRODUCTOS_POR_PAGINA + 1
        for pagina in range(total_paginas):
            inicio = pagina * MAX_PRODUCTOS_POR_PAGINA
            fin = inicio + MAX_PRODUCTOS_POR_PAGINA
            pagina_dict = dict(pagina=pagina + 1, url=f"_from={inicio}&_to={fin}")
            paginas.append(pagina_dict)
            categoria.paginas = paginas
        for marca in data_info['Brands']:
            marca_dict = dict(id=0, nombre=marca['Name'])
            marcas.append(marca_dict)
            categoria.marcas = marcas
        print("categoria " + categoria.name)
        print(f"cant productos {cantidad_productos}")
        print(categoria.paginas)
        for subcategoria in categoria.children:
            urlinfosubcat = f"{URL_BASE}/api/catalog_system/pub/facets/search{subcategoria.url}/?map=c,c"
            data_infosubcat = consumir_api(urlinfosubcat, headers)
            subcategoria.cantidad_productos = data_infosubcat['CategoriesTrees'][0]['Quantity']
            print("sub categoria " + subcategoria.name)
            print(subcategoria.cantidad_productos)
            for subcategoria_2 in subcategoria.children:
                urlinfosubcat_2 = f"{URL_BASE}/api/catalog_system/pub/facets/search{subcategoria.url}/?map=c,c"
                data_infosubcat_2 = consumir_api(urlinfosubcat_2, headers)
                subcategoria_2.cantidad_productos = data_infosubcat_2['CategoriesTrees'][0]['Quantity']
                print("sub categoria 2 " + subcategoria_2.name)
    categorias_y_subcategorias.append(categorias)

    # Guardar los datos parseados en un archivo JSON
    with open('data/categorias.json', 'w', encoding='utf-8') as f:
        json.dump(categorias_y_subcategorias, f, default=convertir_a_dict, ensure_ascii=False, indent=4)


def convertir_a_dict(objeto):
    if isinstance(objeto, CategoriaTemp):
        return objeto.__dict__
    raise TypeError(f"Object of type {objeto.__class__.__name__} is not JSON serializable")


def mapear_categorias():
    # Leer archivo
    data = leer_json(f'{RUTA_DATOS}categorias.json')
    # Crear un nuevo JSON
    nuevo_json = []

    # Configurar el progreso bar
    total_items = len(data[0])
    progress_bar = tqdm(total=total_items, desc="Mapeando Categorías", unit="item")

    # Procesar cada item en el JSON proporcionado
    for item in data[0]:
        # Añadir la categoría principal
        nuevo_json.append({
            "id": item["category_id"],
            "nombre": item["name"]
        })

        # Añadir cada subcategoría
        for subcategoria in item.get("children", []):
            nuevo_json.append({
                "id": subcategoria["category_id"],
                "nombre": subcategoria["name"]
            })

            # Añadir cada subcategoría 2
            for subcategoria_2 in subcategoria.get("children", []):
                nuevo_json.append({
                    "id": subcategoria_2["category_id"],
                    "nombre": subcategoria_2["name"]
                })

        progress_bar.update(1)

    progress_bar.close()

    # Ordenar la lista resultante por id
    nuevo_json = sorted(nuevo_json, key=lambda x: x['id'])
    guardar_json(nuevo_json, f'{RUTA_DATOS}lista_categoria.json')


def actualizar_categorias(archivo_csv):
    categorias = leer_json(f'{RUTA_DATOS}lista_categoria.json')
    # print(categorias)
    filas, nombres_campos = leer_csv(archivo_csv)
    # filas = filas[1:]
    filas_actualizadas = []

    for fila in filas:
        # print(fila)
        # print(nombres_campos)
        categoria_id = int(obtener_valor(fila, 'categoria_id'))
        for categoria in categorias:
            if categoria_id == int(categoria['id']):
                fila['categoria'] = categoria['nombre']
                filas_actualizadas.append(fila)
                break
    print(filas_actualizadas[1])
    actualizar_valores(archivo_csv, filas_actualizadas)

    return filas_actualizadas
