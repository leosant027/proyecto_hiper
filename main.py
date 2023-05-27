import asyncio

import requests
import json

from funciones.categoria import listar_categoria
from funciones.filtros import selecionar_filtro


url = "https://www.hiperlibertad.com.ar/api/catalog_system/pub/category/tree/50"
response = requests.get(url)
listar_categoria(response)
#filtro=selecionar_filtro()
#print(filtro.valor)


