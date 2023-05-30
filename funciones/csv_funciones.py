import csv
import os


def guardar_csv(objeto, archivo):
    """
    Esta función guarda un objeto en un archivo CSV.
    Si el archivo está vacío, primero escribe los nombres de las columnas.
    Luego escribe los valores de los atributos del objeto en una nueva fila.

    Parámetros:
    objeto (Object): El objeto que se va a guardar en el archivo CSV.
    archivo (str): El nombre del archivo CSV en el que se guardará el objeto.
    """
    with open(archivo, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        if os.path.getsize(archivo) == 0:
            nombres_columnas = obtener_nombres_columnas(objeto)
            writer.writerow(nombres_columnas)
        valores_atributos = obtener_valores_atributos(objeto)
        valores_decodificados = [valor.decode('utf-8') if isinstance(valor, bytes) else valor for valor in
                                 valores_atributos]
        writer.writerow(valores_decodificados)


def obtener_nombres_columnas(objeto):
    """
    Esta función devuelve una lista con los nombres de los atributos válidos del objeto.

    Parámetro:
    objeto (Object): El objeto del que se obtendrán los nombres de los atributos válidos.
    """
    return obtener_atributos_validos(objeto)


def obtener_valores_atributos(objeto):
    """
    Esta función devuelve una lista con los valores de los atributos válidos del objeto.

    Parámetro:
    objeto (Object): El objeto del que se obtendrán los valores de los atributos válidos.
    """
    return [getattr(objeto, atributo) for atributo in obtener_atributos_validos(objeto)]


def obtener_atributos_validos(objeto):
    """
    Esta función devuelve una lista con los nombres de los atributos válidos del objeto.
    Un atributo es válido si no es una función y su nombre no comienza con "__".

    Parámetro:
    objeto (Object): El objeto del que se obtendrán los atributos válidos.
    """
    return [atributo for atributo in dir(objeto) if
            not callable(getattr(objeto, atributo)) and not atributo.startswith("__")]


def leer_csv(archivo):
    with open(archivo, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames
