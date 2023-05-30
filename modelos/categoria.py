class Categoria:
    def __init__(self, categoria_id,tiene_subcategoria, nombre, url, cantidad_productos, subcategorias, marcas, paginas):
        self.id = categoria_id
        self.tiene_subcategoria = tiene_subcategoria
        self.nombre = nombre
        self.url = url
        self.cantidad_productos = cantidad_productos
        self.subcategorias = subcategorias
        self.marcas = marcas
        self.paginas = paginas
