import json
from tqdm import tqdm
import concurrent.futures
from costante_gral import URL_BASE, RUTA_BUSQUEDA, RUTA_DATOS, RUTA_INFORMES
from funciones.api import consumir_api
from funciones.csv_funciones import guardar_csv
from funciones.json_funciones import leer_json, guardar_json
from funciones.parses import parse_categoria, parse_produco


def crear_lista_url_productos():
    data = leer_json(f'{RUTA_DATOS}categorias.json')
    productos_urls = []
    for categoria in data[0]:
        categoria_seleccionada = parse_categoria(categoria)
        for pagina in categoria_seleccionada.paginas:
            url_productos = URL_BASE + RUTA_BUSQUEDA + categoria_seleccionada.url + '?' + pagina['url']
            productos_urls.append(url_productos)

    # Guardar las URLs en un archivo JSON
    with open(f'{RUTA_DATOS}urls_productos.json', 'w') as file:
        json.dump(productos_urls, file)


def descargar_productos(sucursal, headers):
    enlaces = leer_json(f'{RUTA_DATOS}urls_productos.json')
    productos_dic = []
    marcas = []

    # Configurar la barra de progreso
    total_enlaces = len(enlaces)
    progress_bar = tqdm(total=total_enlaces, desc="Descargando y ordenando productos", unit="enlace")

    def procesar_producto(producto):
        marca_actual = {'id': producto['brandId'], 'nombre': producto['brand']}
        if marca_actual not in marcas:
            marcas.append(marca_actual)
        productos_dic.append(parse_produco(producto))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for enlace in enlaces:
            future = executor.submit(consumir_api, enlace + f'&sc={sucursal.sucursal_id}', headers)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            productos = future.result()
            for prod in productos:
                executor.submit(procesar_producto, prod)
            progress_bar.update(1)  # Actualizar el progreso de la barra de progreso por cada enlace procesado

    progress_bar.close()  # Cerrar la barra de progreso

    # Ordenar los productos por categoría
    productos_dic = sorted(productos_dic, key=lambda x: x.categoria_id)
    guardar_json(marcas, f'{RUTA_DATOS}lista_marcas.json')
    for elemento in productos_dic:
        guardar_csv(elemento, f'{RUTA_INFORMES}{sucursal.nombre.replace(" ", "-")}.csv')
