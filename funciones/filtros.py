from funciones.json_funciones import crear_menu
from funciones.parses import parse_filtro


def selecionar_filtro():
    opcion_seleccionada = crear_menu("data/filtros.json", "opciones")
    if opcion_seleccionada is not None:
        filtro = parse_filtro(opcion_seleccionada)
        return filtro
