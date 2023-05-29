from modelos.categoria import Categoria
from modelos.categoria_temp import CategoriaTemp
from modelos.filtro import Filtro
from modelos.producto import Producto
from modelos.sucursal import Sucursal


def parse_categorias(data):
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
            categoria.children.append(parse_categorias(child))

    return categoria


def parse_categoria(data):
    categoria = Categoria(
        categoria_id=data["categoria_id"],
        nombre=data["nombre"],
        url=data["url"],
        cantidad_productos=data["cantidad_productos"],
        subcategorias=["subcategorias"],
        marcas=data["marcas"],
        paginas=data["paginas"]
    )
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


def parse_produco(data):
    producto = Producto(
        producto_id=data["productId"],
        nombre=data["productName"],
        marca=data["brand"],
        marca_id=data["brandId"],
        categoria=data["categoryId"],
        precio=data["items"][0]["sellers"][0]["commertialOffer"]["Price"],
        precio_lista=data["items"][0]["sellers"][0]["commertialOffer"]["ListPrice"],
        url=data["link"],
        stock=data["items"][0]["sellers"][0]["commertialOffer"]["AvailableQuantity"],
        sku=data["items"][0]["ean"],
        codigo_barra=data["items"][0]["ean"]
    )
    return producto
