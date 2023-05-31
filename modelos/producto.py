class Producto:
    """
    Esta clase representa un producto en un sistema.

    Atributos:
    - producto_id (int): El identificador único del producto.
    - nombre (str): El nombre del producto.
    - marca_id (int): El identificador único de la marca del producto.
    - marca (str): El nombre de la marca del producto.
    - categoria (str): La categoría del producto.
    - categoria_id (int): El identificador único de la categoría del producto.
    - precio (float): El precio del producto.
    - precio_lista (float): El precio de lista del producto.
    - url (str): La URL del producto.
    - stock (int): La cantidad de stock disponible del producto.
    - sku_id (int): El identificador único del SKU del producto.
    - codigo_barra (str): El código de barras del producto.

    Métodos:
    - __init__(producto_id, nombre, marca_id, marca, categoria, categoria_id, precio,
                precio_lista, url, stock, sku_id, codigo_barra): Inicializa una nueva instancia de la clase Producto.
    """

    def __init__(self, producto_id: int, nombre: str, marca_id: int, marca: str, categoria: str, categoria_id: int,
                 precio: float, precio_lista: float, url: str, stock: int, sku_id: int, codigo_barra: str):
        """
        Inicializa una nueva instancia de la clase Producto.

        Parámetros:
        - producto_id (int): El identificador único del producto.
        - nombre (str): El nombre del producto.
        - marca_id (int): El identificador único de la marca del producto.
        - marca (str): El nombre de la marca del producto.
        - categoria (str): La categoría del producto.
        - categoria_id (int): El identificador único de la categoría del producto.
        - precio (float): El precio del producto.
        - precio_lista (float): El precio de lista del producto.
        - url (str): La URL del producto.
        - stock (int): La cantidad de stock disponible del producto.
        - sku_id (int): El identificador único del SKU del producto.
        - codigo_barra (str): El código de barras del producto.

        No retorna ningún valor.
        """
        self.producto_id = producto_id
        self.nombre = nombre
        self.marca = marca
        self.marca_id = marca_id
        self.categoria = categoria
        self.categoria_id = categoria_id
        self.precio = precio
        self.precio_lista = precio_lista
        self.url = url
        self.stock = stock
        self.sku_id = sku_id
        self.codigo_barra = codigo_barra
