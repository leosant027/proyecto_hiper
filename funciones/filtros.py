from funciones.json_funciones import seleccionar_opcion
from funciones.parses import parse_filtro


def selecionar_filtro():
    opcion_seleccionada=seleccionar_opcion("data/filtros.json","opciones")
    if opcion_seleccionada is not None:
        filtro = parse_filtro(opcion_seleccionada)
        return filtro