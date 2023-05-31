class Sucursal:
    """
    Esta clase representa una sucursal en un sistema.

    Atributos:
    - nombre (str): El nombre de la sucursal.
    - sucursal_id (int): El identificador único de la sucursal.
    - cod (int): El código de la sucursal.

    Métodos:
    - __init__(nombre, sucursal_id, cod): Inicializa una nueva instancia de la clase Sucursal.
    """

    def __init__(self, nombre: str, sucursal_id: int, cod: int):
        """
        Inicializa una nueva instancia de la clase Sucursal.

        Parámetros:
        - nombre (str): El nombre de la sucursal.
        - sucursal_id (int): El identificador único de la sucursal.
        - cod (int): El código de la sucursal.

        No retorna ningún valor.
        """
        self.sucursal_id = sucursal_id
        self.nombre = nombre
        self.cod = cod
