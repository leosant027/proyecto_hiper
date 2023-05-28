from modelos.categoria import Categoria
from modelos.filtro import Filtro
from modelos.sucursal import Sucursal


def parse_categoria(data):
    categoria = Categoria(
        id=data["id"],
        name=data["name"],
        has_children=data["hasChildren"],
        url=data["url"].replace("https://www.hiperlibertad.com.ar", ""),
        children=[],
    )

    # Si la categoría tiene hijos, recorrerlos recursivamente
    if "children" in data:
        for child in data["children"]:
            categoria.children.append(parse_categoria(child))

    return categoria


def parse_sucursal(data):
    sucursal = Sucursal(
        id=data["id"],
        ciudad=data["nombre"],
        cod=data["cod"],
    )
    return sucursal


def parse_filtro(data):
    filtro = Filtro(
        valor=data["valor"],
        nombre=data["nombre"],
    )
    return filtro
