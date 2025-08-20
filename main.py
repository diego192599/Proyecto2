class Producto():
    def __init__(self,codigo_producto,id_categoria,nombre,precio,total_compras,total_ventas,stock):
        self.codigo_producto=codigo_producto
        self.id_categoria=id_categoria
        self.nombre=nombre
        self.precio=precio
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock

    def actualizar_Stock(self,cantidad,tipo):
        if tipo=='compra':
            self.stock+=cantidad
            self.total_compras+=cantidad
        elif tipo=='venta':
            self.stock-=cantidad
            self.total_ventas+=cantidad

class Categorias():
    def __init__(self,id_categoria,nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre

class Cliente():
     def __init__(self,nit,nombre,telefono,direccion,correo):
         self.nit=nit
         self.nombre=nombre
         self.telefono=telefono
         self.direccion=direccion
         self.correo=correo

class Empleado():
    def __init__(self, id_empleado, nombre, telefono, direccion, correo, salario_base):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.salario_base = salario_base
        self.ventas_realizadas = 0

    def calcular_salario(self):
        bono = self.ventas_realizadas * 0.05
        return self.salario_base + bono

class Proveedor():
