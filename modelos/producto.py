class Producto:
    def __init__(self, producto_id, nombre, marca_id, marca, categoria, precio,
                 precio_lista, url, stock, sku, codigo_barra):
        self.producto_id = producto_id
        self.nombre = nombre
        self.marca = marca
        self.marca_id = marca_id
        self.categoria = categoria
        self.precio = precio
        self.precio_lista = precio_lista
        self.url = url
        self.stock = stock
        self.sku = sku
        self.codigo_barra = codigo_barra
