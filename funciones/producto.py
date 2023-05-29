import json

from costante_gral import URL_BASE, RUTA_BUSQUEDA
from funciones.json_funciones import leer_json
from funciones.parses import parse_categoria

def crear_lista_url_productos():
    data = leer_json("data/categorias.json")
    productos_urls = []
    for categoria in data:
        categoria_seleccionada = parse_categoria(categoria)
        for pagina in categoria_seleccionada.paginas:
            url_productos = URL_BASE + RUTA_BUSQUEDA + categoria_seleccionada.url + "?" + pagina['url']
            productos_urls.append(url_productos)

    # Guardar las URLs en un archivo JSON
    with open("data/productos.json", "w") as file:
        json.dump(productos_urls, file)