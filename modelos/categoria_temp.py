class CategoriaTemp:
    def __init__(self, category_id, name, has_children, url, children):
        self.category_id = category_id
        self.name = name
        self.has_children = has_children
        self.url = url
        self.children = children
        self.cantidad_productos = 0
        self.subcategorias = []
        self.marcas = []
        self.paginas = []


def __dict__(self):
    return {
        'category_id': self.category_id,
        'name': self.name,
        'has_children': self.has_children,
        'url': self.url,
        'children': self.children,
        'cantidad_productos': self.cantidad_productos,
        'subcategorias': self.subcategorias,
        'marcas': self.marcas,
        'paginas': self.paginas
    }
