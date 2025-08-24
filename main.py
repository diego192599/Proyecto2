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
    def __init__(self, categoria,ordenado):
        self.productos={}
        self.categoria=categoria
        self.ordenado=ordenado

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

    def ordenar_productos(self):
        if not self.productos:
            print("No hay productos para ordenar.")
            return

        print("\n--- ORDENAR PRODUCTOS ---")
        print("1. Por nombre")
        print("2. Por precio")
        print("3. Por cantidad")
        print("4. Por código")
        opcion = input("Seleccione una opción: ")

        criterios = {"1": "nombre", "2": "precio", "3": "stock", "4": "id_producto"}
        criterio = criterios.get(opcion)
        if not criterio:
            print("Opción inválida.")
            return

        lista_productos = list(self.productos.values())
        ordenados = self.ordenador.quicksort(lista_productos, criterio)

        for p in ordenados:
            print(f"[{p.id_producto}] {p.nombre} | Precio: {p.precio} | Stock: {p.stock}")

class OrdenadorProductos:
    def quicksort(self, lista, criterio):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            if criterio == "nombre":
                menores = [x for x in lista[1:] if x.nombre.lower() <= pivote.nombre.lower()]
                mayores = [x for x in lista[1:] if x.nombre.lower() > pivote.nombre.lower()]
            elif criterio == "precio":
                menores = [x for x in lista[1:] if x.precio <= pivote.precio]
                mayores = [x for x in lista[1:] if x.precio > pivote.precio]
            elif criterio == "stock":
                menores = [x for x in lista[1:] if x.stock <= pivote.stock]
                mayores = [x for x in lista[1:] if x.stock > pivote.stock]
            elif criterio == "id_producto":
                menores = [x for x in lista[1:] if x.id_producto <= pivote.id_producto]
                mayores = [x for x in lista[1:] if x.id_producto > pivote.id_producto]
            else:
                return lista

            return self.quicksort(menores, criterio) + [pivote] + self.quicksort(mayores, criterio)

class Cliente():
     def __init__(self,nit,nombre,telefono,correo):
         self.nit=nit
         self.nombre=nombre
         self.telefono=telefono
         self.correo=correo

class Gestion_Cliente:
    def __init__(self):
        self.clientes={}
    def Agregar_Cliente(self):
        id_cliente=input("Ingrese el ID del cliente: ")
        nombre=input("Ingrese su nombre: ")
        telefono=input("Ingrese su numero de telefono: ")
        correo=input("Ingrese su correo electronico personal: ")
        self.clientes[id_cliente]=Cliente(id_cliente,nombre,telefono,correo)
        print(f"El cliente {nombre} se agrego correctamente")

    def mostrar(self):
        if not self.clientes:
            print("No hay clientes")
            return
        for c in self.clientes:
            print(c.mostrar_info())

    def buscar_Clientes(self):
        criterio=input("Ingrese el nombre o ID del cliente: ").lower()
        encotrados=[c for c in self.clientes.values()
                    if criterio in c.nombre.lower() or criterio==c.id_cliente]
        if encotrados:
            for c in encotrados:
                print(c.mostrar_info())
        else:
            print("Cliente no encontrado")


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

class Gestion_empleado:
    contador=0
    def __init__(self,admin):
        self.empleados={}
        self.admin=admin

    def agregar_empleado(self):
        if not self.admin.verificar_password():
            print("Solo el Adminiistrador puede agregar empleados")
            return
        Gestion_empleado.contador+=1
        print(f"\n---Agregar Empleado{Gestion_empleado.contador}---")
        id_empledado=input("Ingrese la ID del nuevo empleado: ")
        nombre=input("Nombre del empleado: ")
        telefono=input("El numero que nos servira para contactarlo: ")
        direccion=input("Ingrese la direccion: ")
        correo=input("Ingrese el correo personal del empleado: ")
        saliro_base=float(input("Ingrese el salario que recibira el empleado: "))
        nuevo=Empleado(id_empledado,nombre,telefono,direccion,correo,saliro_base)
        self.empleados[id_empledado]=nuevo
        print(f"Empleado {nombre} agregado correctamente")
    def mostrar_empleado(self):
        if not self.empleados:
            print("No hay empleados registrados")
            return
        for e in self.empleados.values():
            print(e.mostrar_info())
    def buscar_empleado(self):
        criterio=input("Ingrese el ID o nombre: ").lower()
        encontrados=[
            e for e in self.empleados.values()
            if criterio in e.nombre.lower() or criterio==e.id_empleado
        ]
        if encontrados:
            for e in encontrados:
                print(e.mostrar_info())
        else:
            print("Empleado no encontrado")

    def despedir_empleado(self):
        id_empleado=input("Ingrese el ID del empleado a despedir: ")
        if id_empleado in self.empleados:
          self.empleados[id_empleado]="Despedido"
          print(f"Empleado {self.empleados[id_empleado].nombre} a sido despedido")
        else:
            print("No hay ningun empleado con ese ID")

class Proveedor():
    def __init__(self,id_provedor,nombre,empresa,telefono,direccion,correo,id_categoria):
        self.id_provedor=id_provedor
        self.nombre=nombre
        self.empresa=empresa
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.id_categoria=id_categoria
class Gestion_Proveedor:
    def __init__(self,categoria):
        self.proveedores={}
        self.categoria=categoria
        self.contador_proveedores=0


    def agregar(self):
        id_proveedor=input("Ingrese el id del proveedor: ")
        if id_proveedor in self.proveedores:
            print("El proveedor ya fue registrado")
            return
        nombre=input("Ingrese el nombre: ")
        empresa=input("Ingrese la empresa del la cual viene: ")
        telefono=input("Telefono: ")
        direccion=input("Ingrese la direccion de donde proviene: ")
        correo=input("Ingrese el correo de la empresa: ")
        id_categoria=input("Ingrese la ID de la categoria: ")
        if id_categoria not in self.categoria:
            print("La categoria no existe")
            return
        self.proveedores[id_proveedor]=Proveedor(id_proveedor,nombre,empresa,telefono,direccion,correo,id_categoria)
        self.contador_proveedores+=1
        print("Se agrego correctamente el proveedor")
        print(f"Total de proveedores registrados: {self.contador_proveedores}")

    def listar(self):
        if not self.proveedores:
            print("No hay proveedores")
            return
        for p in self.proveedores.values():
            cat=self.categoria[p.id_categoria].nombre
            print(f"[{p.id_proveedor}] {p.nombre} ({p.empresa}) - Categoría: {cat}")

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
        total = 0
        for d in self.detalles:
            total += d.subtotal
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

class Gestion_compra:
    def __init__(self,productos,proveedores):
        self.compras={}
        self.productos=productos
        self.proveedores=proveedores

    def registrar_compras(self):
        id_compra=input("ID compras: ")
        fecha=input("Fecha de Vencimiento (YYYY/MM/DD): ")
        id_proveedor=input("Ingrese ID proveedor: ")
        id_empleado=input("Ingrese ID Empleado: ")
        if id_proveedor not in self.proveedores:
            print("No existe ese proveedor")
            return
        compra=Compra(id_compra,fecha,id_proveedor,id_empleado)
        while True:
            codigo_producto = input("Código del producto (o 'fin' para terminar): ")
            if codigo_producto.lower() == 'fin':
                break
            if codigo_producto not in self.productos:
                print("Producto no encontrado.")
                continue

            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio de compra: "))
            fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")

            detalle = DetalleCompra(len(compra.detalles) + 1, id_compra, codigo_producto, cantidad, precio,
                                    fecha_caducidad)
            compra.agregar_detalle(detalle)

            self.productos[codigo_producto].stock += cantidad
            self.productos[codigo_producto].total_compras += cantidad

        self.compras[id_compra] = compra
        print(f"Compra registrada. Total: {compra.calcular_total()}")
