from funciones.parses import parse_categoria



def listar_categoria(response):
    if response.status_code == 200:
        data = response.json()
        categorias = []
        # Crear objetos Categoria a partir de los datos obtenidos
        for category_data in data:
            categorias.append(parse_categoria(category_data))

        # Imprimir la lista de categorías
        for categoria in categorias:
            print(f"Nombre: {categoria.name}, ID: {categoria.id},")
            for subcategoria in categoria.children:
                print(f" {subcategoria.name}, ID: {subcategoria.id},")
    else:
        print(f"Error al recuperar datos: {response.status_code}")