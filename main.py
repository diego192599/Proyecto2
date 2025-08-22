class Categorias():
    def __init__(self,id_categoria,nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre

class Producto():
    def __init__(self,codigo_producto,id_categoria,nombre,precio,total_compras,total_ventas,stock):
        self.codigo_producto=codigo_producto
        self.id_categoria=id_categoria
        self.nombre=nombre
        self.precio=precio
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock

    def actualizar_stock(self, cantidad, tipo):
        if tipo == 'compra':
            self.stock += cantidad
            self.total_compras += cantidad
        elif tipo == 'venta':
            if self.stock >= cantidad:
                self.stock -= cantidad
                self.total_ventas += cantidad
                return True
            else:
                print("Error: No hay suficiente stock para la venta.")
                return False
class Gestion_Procudctos:
    contador=0
    limite_Stock=50
    def __init__(self, categoria):
        self.productos={}
        self.categoria=categoria

    def agregar_Producto(self):
        while True:
            Gestion_Procudctos.contador += 1
            print(f"\n--- Agregar Producto{Gestion_Procudctos.contador} ---")

            codigo_producto = input("Código del producto: ")
            id_categoria = input("ID de categoría: ")

            if id_categoria not in self.categoria:
                print("Error: La categoría no existe. Agrega primero la categoría.")
                continue

            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))

            nuevo_producto = Producto(codigo_producto, id_categoria, nombre, precio, 0, 0, 0)
            self.productos[codigo_producto] = nuevo_producto

            print(f"Producto '{nombre}' agregado correctamente con stock inicial en 0.")

            continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
            if continuar != 's':
                break
    def mostrar_info(self):
        if not self.productos:
            print("No hay productos registrados")
            return
        for p  in self.productos.values():
            categorias=self.categoria[p.id_categoria]
            print(f"[{p.codigo_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {categorias.nombre} | Stock: {p.stock}")

    def eliminar(self):
        if not self.productos:
            print("No hay productos")
            return
        print("1. Eliminar por codigo")
        print("2. Eliminar por maximo de stock")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            codigo=input("Ingrese el codigo a eliminar: ")
            if codigo in self.productos:
                del self.productos[codigo]
                print("Producto eliminado")
            else:
                print("Producto no encontrado")
        elif opcion=="2":
            eliminar=[codigo for codigo , prod in self.productos.items()
                      if prod.stock>Gestion_Procudctos.limite_Stock]
            for codigo in eliminar:
                del self.productos[codigo]
            print(f"{len(eliminar)} productos eliminados correctamente")
        else:
            print("Opcion no valida")

    def buscar(self):
        if not self.productos:
            print("No hay productos")
            return
        criterio=input("Ingrese el nombre o codigo del producto a buscar: ").lower()
        encontrados=[p for p in self.productos.values()
                     if criterio in p.nombre.lower or criterio==p.codigo_productos]
        if encontrados:
            for prod in encontrados:
                print(f"{prod.codigo_productos}- {prod.nombre}- Stock: {prod.stock}")
        else:
            print("Productos no encontrados")

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

    def mostrar_info(self):
        return f"{self.id_empleado}- {self.nombre}- Salario: {self.calcular_salario():.2f}"
class Administrado(Empleado):
    def __init__(self, id_empleado, nombre, telefono, direccion, correo, salario_base, password):
        super().__init__(id_empleado, nombre, telefono, direccion, correo, salario_base)
        self.password = password
    def verificar_password(self,password_ingresada):
        print("Veridicar si usted es administrador")
        return self.password==password_ingresada

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