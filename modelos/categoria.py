class Categoria:
    """
    Esta es una clase que representa una categoría.

    Atributos:
        id (int): El identificador único de la categoría.
        tiene_subcategoria (bool): Indica si la categoría tiene subcategorías.
        nombre (str): El nombre de la categoría.
        url (str): La URL asociada con la categoría.
        cantidad_productos (int): El número de productos en la categoría.
        subcategorias (list): Una lista de subcategorías asociadas con la categoría.
        marcas (list): Una lista de marcas asociadas con la categoría.
        paginas (list): El número de páginas en la categoría.

    Métodos:
        __init__(categoria_id, tiene_subcategoria, nombre, url, cantidad_productos, subcategorias, marcas, paginas):
            El constructor de la clase Categoría.
    """

    def __init__(self, categoria_id: int, tiene_subcategoria: bool, nombre: str, url: str,
                 cantidad_productos: int, subcategorias: list, marcas: list, paginas: list):
        """
        El constructor de la clase Categoría.

        Parametros:
           categoria_id (int): El identificador único de la categoría.
           tiene_subcategoria (bool): Indica si la categoría tiene subcategorías.
           nombre (str): El nombre de la categoría.
           url (str): La URL asociada con la categoría.
           cantidad_productos (int): El número de productos en la categoría.
           subcategorias (list): Una lista de subcategorías asociadas con la categoría.
           marcas (list): Una lista de marcas asociadas con la categoría.
           paginas (list): Una lista de páginas en la categoría que se usarán para generar los enlaces.

        No retorna ningún valor.
        """

        self.id = categoria_id
        self.tiene_subcategoria = tiene_subcategoria
        self.nombre = nombre
        self.url = url
        self.cantidad_productos = cantidad_productos
        self.subcategorias = subcategorias
        self.marcas = marcas
        self.paginas = paginas
