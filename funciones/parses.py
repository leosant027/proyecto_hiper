from modelos.categoria import Categoria
from modelos.categoria_temp import CategoriaTemp
from modelos.filtro import Filtro
from modelos.producto import Producto
from modelos.sucursal import Sucursal


def parse_categoria_temp(data):
    categoria = CategoriaTemp(
        category_id=data["id"],
        name=data["name"],
        has_children=data["hasChildren"],
        url=data["url"].replace("https://www.hiperlibertad.com.ar", ""),
        children=[],
    )

    # Si la categoría tiene hijos, recorrerlos recursivamente
    if "children" in data:
        for child in data["children"]:
            categoria.children.append(parse_categoria_temp(child))

    return categoria


def parse_categoria(data):
    categoria = Categoria(
        categoria_id=data["category_id"],
        tiene_subcategoria=data["has_children"],
        nombre=data["name"],
        url=data["url"],
        cantidad_productos=data["cantidad_productos"],
        subcategorias=["children"],
        marcas=data["marcas"],
        paginas=data["paginas"]
    )
    return categoria


def parse_sucursal(data):
    sucursal = Sucursal(
        sucursal_id=data["id"],
        nombre=data["nombre"],
        cod=data["cod"],
    )
    return sucursal


def parse_filtro(data):
    filtro = Filtro(
        valor=data["valor"],
        nombre=data["nombre"],
    )
    return filtro


def parse_produco(data):
    producto = Producto(
        producto_id=data["productId"],
        nombre=data["productName"],
        marca=data["brand"],
        marca_id=data["brandId"],
        categoria="",
        categoria_id=data["categoryId"],
        precio=data["items"][0]["sellers"][0]["commertialOffer"]["Price"],
        precio_lista=data["items"][0]["sellers"][0]["commertialOffer"]["ListPrice"],
        url=data["link"],
        stock=data["items"][0]["sellers"][0]["commertialOffer"]["AvailableQuantity"],
        sku_id=data["items"][0]["itemId"],
        codigo_barra=data["items"][0]["ean"]
    )
    return producto
