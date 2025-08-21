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
    def __init__(self,id_provedor,nombre,empresa,telefono,direccion,correo,id_categoria):
        self.id_provedor=id_provedor
        self.nombre=nombre
        self.empresa=empresa
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.id_categoria=id_categoria

class Venta:
    def __init__(self, id_venta, fecha, nit_cliente, id_empleado):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit_cliente = nit_cliente
        self.id_empleado = id_empleado
        self.detalles = []

    def calcular_total(self):
        return sum(detalle.subtotal for detalle in self.detalles)


class DetalleVenta:
    def __init__(self, id_detalle, id_venta, codigo_producto, cantidad, precio):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = cantidad * precio


class Compra():
    def __init__(self, id_compra, fecha, id_proveedor, id_empleado):
        self.id_compra = id_compra
        self.fecha = fecha
        self.id_proveedor = id_proveedor
        self.id_empleado = id_empleado
        self.detalles = []

    def calcular_total(self):
        total=0
        for detalle in self.detalles:
            total=total+detalle.subtotal
        return total

class DetalleCompra:
    def __init__(self, id_detalle, id_compra, codigo_producto, cantidad, precio_compra, fecha_caducidad):
        self.id_detalle = id_detalle
        self.id_compra = id_compra
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.fecha_caducidad = fecha_caducidad
        self.subtotal = cantidad * precio_compra
