class Categoria:
    def __init__(self, categoria_id, nombre, url, cantidad_productos, subcategorias, marcas, paginas):
        self.id = categoria_id
        self.nombre = nombre
        self.url = url
        self.cantidad_productos = cantidad_productos
        self.subcategorias = subcategorias
        self.marcas = marcas
        self.paginas = paginas
