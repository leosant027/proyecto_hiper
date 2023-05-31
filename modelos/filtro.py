class Filtro:
    """
    Esta es una clase que representa un filtro.

    Atributos:
        valor (int): Representa el valor asociado con el filtro.
        nombre (str): Representa el nombre del filtro.
    """

    def __init__(self, valor: int, nombre: str):
        """
        El constructor de la clase Filtro.

        Parametros:
           valor (str): El valor que se quiere asignar al filtro.
           nombre (str): El nombre del filtro.
        """

        self.valor = valor
        self.nombre = nombre
