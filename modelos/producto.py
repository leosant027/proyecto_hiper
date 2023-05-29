class Producto:
    def __init__(self, producto_id, nombre, marca_id, marca, categoria, categoria_id, precio,
                 precio_lista, url, stock, sku_id, codigo_barra):
        self.producto_id = producto_id
        self.nombre = nombre
        self.marca = marca
        self.marca_id = marca_id
        self.categoria = categoria
        self.categoria_id = categoria_id
        self.precio = precio
        self.precio_lista = precio_lista
        self.url = url
        self.stock = stock
        self.sku_id = sku_id
        self.codigo_barra = codigo_barra
