class Marca:
    """
    Esta clase representa una marca de producto.

    Atributos:
    - id (int): El identificador único de la marca.
    - nombre (str): El nombre de la marca.

    Métodos:
    - __init__(marca_id, nombre): Inicializa una nueva instancia de la clase Marca.
    """

    def __init__(self, marca_id: int, nombre: str):
        """
        Inicializa una nueva instancia de la clase Marca.

        Parámetros:
        - marca_id (int): El identificador único de la marca.
        - nombre (str): El nombre de la marca.

        No retorna ningún valor.
        """
        self.marca_id = marca_id
        self.nombre = nombre
