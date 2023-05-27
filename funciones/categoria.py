from funciones.parses import parse_categoria
import json


def listar_categoria(response):
    if response.status_code == 200:
        data = response.json()
        categorias = []
        # Crear objetos Categoria a partir de los datos obtenidos
        for category_data in data:
            categorias.append(parse_categoria(category_data))
        categorias_y_subcategorias = []
        # Imprimir la lista de categorías
        for categoria in categorias:
            categoria_dict = {
                "nombre": categoria.name,
                "id": categoria.id,
                "url": categoria.url,
                "subcategorias": []
            }
            for subcategoria in categoria.children:
                subcategoria_dict = {
                    "id": subcategoria.id,
                    "nombre": subcategoria.name,
                    "url": subcategoria.url
                }
                categoria_dict["subcategorias"].append(subcategoria_dict)
            categorias_y_subcategorias.append(categoria_dict)
        with open('data/categorias.json', 'w', encoding='utf-8') as f:
            json.dump(categorias_y_subcategorias, f, ensure_ascii=False, indent=4)
    else:
        print(f"Error al recuperar datos: {response.status_code}")
