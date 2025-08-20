class Producto():
    def __init__(self,codigo_producto,id_categoria,nombre,precio,total_compras,total_ventas,stock):
        self.codigo_producto=codigo_producto
        self.id_categoria=id_categoria
        self.nombre=nombre
        self.precio=precio
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock

    def __str__(self):
        return f"Codigo{self.codigo_producto} - Nombre: {self.nombre} - Precio: {self.precio} "

class Categorias():
    def __init__(self,id_categoria,nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre

    def __str__(self):
        return f"Id Categoria: {self.id_categoria}- Nombre de la categoria: {self.nombre}"

class Cliente():
