from costante_gral import RUTA_INFORMES
from funciones.categoria import listar_categoria, mapear_categorias, actualizar_categorias
from funciones.json_funciones import crear_menu

from funciones.marca import actualizar_marcas
from funciones.parses import parse_sucursal

from funciones.producto import descargar_productos, crear_lista_url_productos

ciudad = crear_menu('data/sucursales.json', key_menu='ciudad')
sucursal = crear_menu(ciudad, atributo='tiendas', key_menu='nombre')
sucursal = parse_sucursal(sucursal)
print(sucursal.nombre)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": f"janus_sid=0cdf9235-95b0-4162-841f-9ea0ada6bc44; VtexRCMacIdv7=251da268-3d8a-46bb-9489-29d86c6e222c; "
              f"checkout.vtex.com=__ofid=36e933c24fb84a789decd5d4b5b173f8; "
              f"CheckoutOrderFormOwnership=67eb7b7e8f804e03b9711ec6a96229df; "
              f"vtex_session"
              f"1=eyJhbGciOiJFUzI1NiIsImtpZCI6IkJCNzM1NTQ4RTJEQzVDNjI5MTA0N0MwRjAwOTQyRENEMUIwOUM2RUYiLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiODE2NGY2MTgtZTg1My00NzdkLTkyNjMtZGQwYWM4MTc0NjZiIiwiaWQiOiIxNjc0ZjM5Ni0zZTlkLTQzZGMtODg5Ny04YzU2ZmRmMzE5ZWMiLCJ2ZXJzaW9uIjo0Niwic3ViIjoic2Vzc2lvbiIsImFjY291bnQiOiJzZXNzaW9uIiwiZXhwIjoxNjg1OTE1MjAyLCJpYXQiOjE2ODUyMjQwMDIsImlzcyI6InRva2VuLWVtaXR0ZXIiLCJqdGkiOiI4MzBmNzk4ZS1kNWNkLTQxOGItYmUwZS02Zjc2MjIyMWYzNjYifQ.QnAb3gIsvASYkcayruYSxeTa6d3hR-iWQWLfqavvjxrVb36mthrYQO2KuZqnH5nVqn8ZlprDHElp7hc_kOLYeQ; vtex_segment=eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIyIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjpudWxsLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkFSUyIsImN1cnJlbmN5U3ltYm9sIjoiJCIsImNvdW50cnlDb2RlIjoiQVJHIiwiY3VsdHVyZUluZm8iOiJlcy1BUiIsImFkbWluX2N1bHR1cmVJbmZvIjoiZXMtQVIiLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9; locale=es-AR; SGTS=98F10D8385C58AAEB67806CC34BE7444; ISSMB=ScreenMedia=0&UserAcceptMobile=False; i18next=es; VtexRCSessionIdv7=d21ffe5d-707a-4e93-8aa0-fc7de5acb426; VTEXSC=sc={sucursal.sucursal_id}; userSelectedStore=true; store-name=C%25C3%2593RDOBA%2520-%2520Hipermercado%2520Rivera; store-sale-channel={sucursal.sucursal_id}; storeSelectorId={sucursal.cod}",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

listar_categoria(headers)
mapear_categorias()
crear_lista_url_productos()
descargar_productos(sucursal, headers)
actualizar_marcas()
sucursal_archivo = RUTA_INFORMES + sucursal.nombre.replace(" ", "-")
actualizar_categorias(f"{sucursal_archivo}.csv")
