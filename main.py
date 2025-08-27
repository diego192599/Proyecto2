class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre


class Producto:
    def __init__(self, codigo_producto, id_categoria, nombre, precio, total_compras, total_ventas, stock):
        self.codigo_producto = codigo_producto
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.precio = precio
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

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
    contador = 0
    limite_Stock = 50

    def __init__(self, categoria, ordenado):
        self.productos = {}
        self.categoria = categoria
        self.ordenado = ordenado

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
        for p in self.productos.values():
            categorias = self.categoria[p.id_categoria]
            print(
                f"[{p.codigo_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {categorias.nombre} | Stock: {p.stock}")

    def eliminar(self):
        if not self.productos:
            print("No hay productos")
            return
        print("1. Eliminar por codigo")
        print("2. Eliminar por maximo de stock")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            codigo = input("Ingrese el codigo a eliminar: ")
            if codigo in self.productos:
                del self.productos[codigo]
                print("Producto eliminado")
            else:
                print("Producto no encontrado")
        elif opcion == "2":
            eliminar = [codigo for codigo, prod in self.productos.items()
                        if prod.stock > Gestion_Procudctos.limite_Stock]
            for codigo in eliminar:
                del self.productos[codigo]
            print(f"{len(eliminar)} productos eliminados correctamente")
        else:
            print("Opcion no valida")

    def buscar(self):
        if not self.productos:
            print("No hay productos")
            return
        criterio = input("Ingrese el nombre o codigo del producto a buscar: ").lower()
        encontrados = [p for p in self.productos.values()
                       if criterio in p.nombre.lower or criterio == p.codigo_productos]
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


class Gestion_Categorias:
    def __init__(self):
        self.categorias = {}

    def agregar_categoria(self):
        id_categoria = input("Ingrese el ID de la categoría: ")
        nombre = input("Ingrese el nombre de la categoría: ")
        if id_categoria in self.categorias:
            print("La categoría ya existe.")
        else:
            self.categorias[id_categoria] = Categorias(id_categoria, nombre)
            print(f"Categoría '{nombre}' agregada correctamente.")

    def mostrar_categorias(self):
        if not self.categorias:
            print("No hay categorías registradas.")
            return
        for cat in self.categorias.values():
            print(f"[{cat.id_categoria}] {cat.nombre}")

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

    def quicksort_clientes(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            menores = [x for x in lista[1:] if x.total_compras <= pivote.total_compras]
            mayores = [x for x in lista[1:] if x.total_compras > pivote.total_compras]
            return self.quicksort_clientes(menores) + [pivote] + self.quicksort_clientes(mayores)


class Cliente:
    def __init__(self, id_cliente, nombre, correo, total_compras=0, descuento=0):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.total_compras = total_compras
        self.descuento = descuento


class Gestion_Cliente:
    def __init__(self, ordenador):
        self.clientes = {}
        self.ordenador = ordenador

    def Agregar_Cliente(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        nombre = input("Ingrese su nombre: ")
        telefono = input("Ingrese su numero de telefono: ")
        correo = input("Ingrese su correo electronico personal: ")
        self.clientes[id_cliente] = Cliente(id_cliente, nombre, telefono, correo)
        print(f"El cliente {nombre} se agrego correctamente")

    def asignar_descuento(self, id_cliente, porcentaje):
        if id_cliente in self.clientes:
            self.clientes[id_cliente].descuento = porcentaje
            print(f"Descuento de {porcentaje}% asignado a {self.clientes[id_cliente].nombre}.")
        else:
            print("Cliente no encontrado.")

    def listar_ordenados_por_compras(self):
        lista_clientes = list(self.clientes.values())
        ordenados = self.ordenador.quicksort_clientes(lista_clientes)
        for c in ordenados:
            print(f"{c.nombre} - Compras: {c.total_compras} - Descuento: {c.descuento}%")

    def mostrar(self):
        if not self.clientes:
            print("No hay clientes")
            return
        for c in self.clientes:
            print(c.mostrar_info())

    def buscar_Clientes(self):
        criterio = input("Ingrese el nombre o ID del cliente: ").lower()
        encotrados = [c for c in self.clientes.values()
                      if criterio in c.nombre.lower() or criterio == c.id_cliente]
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

    def verificar_password(self, password_ingresada):
        print("Veridicar si usted es administrador")
        return self.password == password_ingresada


class Gestion_empleado:
    contador = 0

    def __init__(self, admin):
        self.empleados = {}
        self.admin = admin

    def agregar_empleado(self):
        if not self.admin.verificar_password():
            print("Solo el Adminiistrador puede agregar empleados")
            return
        Gestion_empleado.contador += 1
        print(f"\n---Agregar Empleado{Gestion_empleado.contador}---")
        id_empledado = input("Ingrese la ID del nuevo empleado: ")
        nombre = input("Nombre del empleado: ")
        telefono = input("El numero que nos servira para contactarlo: ")
        direccion = input("Ingrese la direccion: ")
        correo = input("Ingrese el correo personal del empleado: ")
        saliro_base = float(input("Ingrese el salario que recibira el empleado: "))
        nuevo = Empleado(id_empledado, nombre, telefono, direccion, correo, saliro_base)
        self.empleados[id_empledado] = nuevo
        print(f"Empleado {nombre} agregado correctamente")

    def mostrar_empleado(self):
        if not self.empleados:
            print("No hay empleados registrados")
            return
        for e in self.empleados.values():
            print(e.mostrar_info())

    def buscar_empleado(self):
        criterio = input("Ingrese el ID o nombre: ").lower()
        encontrados = [
            e for e in self.empleados.values()
            if criterio in e.nombre.lower() or criterio == e.id_empleado
        ]
        if encontrados:
            for e in encontrados:
                print(e.mostrar_info())
        else:
            print("Empleado no encontrado")

    def despedir_empleado(self):
        id_empleado = input("Ingrese el ID del empleado a despedir: ")
        if id_empleado in self.empleados:
            self.empleados[id_empleado] = "Despedido"
            print(f"Empleado {self.empleados[id_empleado].nombre} a sido despedido")
        else:
            print("No hay ningun empleado con ese ID")


class Proveedor():
    def __init__(self, id_provedor, nombre, empresa, telefono, direccion, correo, id_categoria):
        self.id_provedor = id_provedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria


class Gestion_Proveedor:
    def __init__(self, categoria):
        self.proveedores = {}
        self.categoria = categoria
        self.contador_proveedores = 0

    def agregar(self):
        id_proveedor = input("Ingrese el id del proveedor: ")
        if id_proveedor in self.proveedores:
            print("El proveedor ya fue registrado")
            return
        nombre = input("Ingrese el nombre: ")
        empresa = input("Ingrese la empresa del la cual viene: ")
        telefono = input("Telefono: ")
        direccion = input("Ingrese la direccion de donde proviene: ")
        correo = input("Ingrese el correo de la empresa: ")
        id_categoria = input("Ingrese la ID de la categoria: ")
        if id_categoria not in self.categoria:
            print("La categoria no existe")
            return
        self.proveedores[id_proveedor] = Proveedor(id_proveedor, nombre, empresa, telefono, direccion, correo,
                                                   id_categoria)
        self.contador_proveedores += 1
        print("Se agrego correctamente el proveedor")
        print(f"Total de proveedores registrados: {self.contador_proveedores}")

    def listar(self):
        if not self.proveedores:
            print("No hay proveedores")
            return
        for p in self.proveedores.values():
            cat = self.categoria[p.id_categoria].nombre
            print(f"[{p.id_proveedor}] {p.nombre} ({p.empresa}) - Categoría: {cat}")

class DetalleVenta:
    def __init__(self, id_detalle, id_venta, codigo_producto, cantidad, precio):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio = precio

    def calcular_Subtotal(self):
        return self.cantidad*self.precio

class Venta:
    def __init__(self, id_venta, fecha, nit_cliente, id_empleado):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit_cliente = nit_cliente
        self.id_empleado = id_empleado
        self.detalles = []

    def agregar_datelle(self,detalle):
        self.detalles.append(detalle)

    def calcular_Total(self):
        total=0
        for r in self.detalles:
            total+r.calcular_subtotal()
        return total


class Compra:
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

class gestion_detalles:
    def __init__(self,productos):
        self.productos=productos

    def registrar_detalles(self, compra=None):
        detalles_temporales=[]
        while True:
            codigo_producto=input("Ingrese el codigo del producto(o 'fin' para terminar): ")
            if codigo_producto.lower()=='fin':
                break
            if codigo_producto not in self.productos:
                print("Producto no encontrado")
                continue
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio de compra: "))
            fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")

            detalle = DetalleCompra(
                id_detalle=len(detalles_temporales) + 1,
                id_compra=compra.id_compra,
                codigo_producto=codigo_producto,
                cantidad=cantidad,
                precio_compra=precio,
                fecha_caducidad=fecha_caducidad
            )
            detalles_temporales.append(detalle)

        if not detalles_temporales:
            print("No se ingresaron detalles.")
            return

        print("\nResumen de los detalles ingresados:")
        for d in detalles_temporales:
            print(f"- {d.codigo_producto} | Cantidad: {d.cantidad} | Subtotal: {d.subtotal}")

        confirmar = input("¿Desea confirmar la compra? (s/n): ").lower()
        if confirmar == 's':
            for d in detalles_temporales:
                compra.agregar_detalle(d)
                self.productos[d.codigo_producto].stock += d.cantidad
                self.productos[d.codigo_producto].total_compras += d.cantidad
            print("Detalles confirmados y stock actualizado.")
        else:
            print("Detalles descartados. No se actualizó el stock.")


class Gestion_compra:
    def __init__(self, productos, proveedores):
        self.compras = {}
        self.productos = productos
        self.proveedores = proveedores

    def registrar_compras(self):
        id_compra = input("ID compras: ")
        fecha = input("Fecha de la compra (YYYY/MM/DD): ")
        id_proveedor = input("Ingrese ID proveedor: ")
        id_empleado = input("Ingrese ID Empleado: ")

        if id_proveedor not in self.proveedores:
            print("No existe ese proveedor")
            return

        compra = Compra(id_compra, fecha, id_proveedor, id_empleado)

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

            detalle = DetalleCompra(
                id_detalle=len(compra.detalles) + 1,
                id_compra=id_compra,
                codigo_producto=codigo_producto,
                cantidad=cantidad,
                precio_compra=precio,
                fecha_caducidad=fecha_caducidad
            )

            compra.agregar_detalle(detalle)
            self.productos[codigo_producto].stock += cantidad
            self.productos[codigo_producto].total_compras += cantidad

        self.compras[id_compra] = compra
        print(f"Compra registrada. Total: {compra.calcular_total()}")

class Pagos:
    def __init__(self,id_pago,id_venta,tipo_pago,monto,referencia=None):
        self.id_pago=id_pago
        self.id_venta=id_venta
        self.tipo_pago=tipo_pago
        self.monto=monto
        self.referencia=referencia

class Gestion_pago:
    def __init__(self,ventas):
        self.pagos={}
        self.ventas=ventas

    def registrar_Pagos(self):
        id_pago=input("ID del pago: ")
        id_venta=input("ID de venta a pagar: ")

        if id_venta not in self.ventas:
            print("La venta no existe")
            return
        tipo_pago=input("Tipo de pago (efectivo/tarjeta): ").lower()
        monto=float(input("Monto a pagar: "))
        referencia=None
        if tipo_pago == "tarjeta":
            referencia = input("Últimos 3 dígitos de la tarjeta: ")

            try:
                int(referencia)
            except ValueError:
                print("La referencia debe ser numérica.")
                return

            if len(referencia) != 3:
                print("La referencia debe tener exactamente 3 dígitos.")
                return

        pago = Pagos(id_pago, id_venta, tipo_pago, monto, referencia)
        self.pagos[id_pago] = pago
        print("Pago registrado correctamente.")


class Menu:
    def __init__(self, gestion_productos, gestion_clientes, gestion_empleados, gestion_proveedores, gestion_compras, gestion_ventas,gestion_pagos):
        self.gestion_productos = gestion_productos
        self.gestion_clientes = gestion_clientes
        self.gestion_empleados = gestion_empleados
        self.gestion_proveedores = gestion_proveedores
        self.gestion_compras = gestion_compras
        self.gestion_ventas = gestion_ventas
        self.gestion_pagos=gestion_pagos

    def mostrar_menu(self):
        while True:
            print("\n=== SISTEMA DE FARMACIA ===")
            print("1. Administrador")
            print("2. Empleado")
            print("3. Cliente")
            print("4. Proveedor")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.menu_admin()
                case "2":
                    self.menu_empleado()
                case "3":
                    self.menu_cliente()
                case "4":
                    self.menu_proveedor()
                case "5":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opción inválida.")

    # ------------------ MENÚ ADMIN ------------------
    def menu_admin(self):
        clave = input("Ingrese la contraseña de administrador: ")
        if clave != "admin123":
            print("Contraseña incorrecta.")
            return

        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Gestionar productos")
            print("2. Gestionar empleados")
            print("3. Gestionar proveedores")
            print("4. Ver compras registradas")
            print("5. Ver pagos registrados")
            print("6. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_productos.menu_productos()
                case "2":
                    self.gestion_empleados.menu_empleados()
                case "3":
                    self.gestion_proveedores.menu_proveedores()
                case "4":
                    self.gestion_compras.mostrar_compras()
                case "5":
                    self.gestion_pagos.mostrar_pagos()
                case "6":
                    break
                case _:
                    print("Opción inválida.")

    # ------------------ MENÚ EMPLEADO ------------------
    def menu_empleado(self):
        while True:
            print("\n--- MENÚ EMPLEADO ---")
            print("1. Registrar venta")
            print("2. Registrar compra")
            print("3. Registrar pago")
            print("4. Ver productos")
            print("5. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_ventas.registrar_venta()
                case "2":
                    self.gestion_compras.registrar_compras()
                case "3":
                    self.gestion_pagos.registrar_pago()
                case "4":
                    self.gestion_productos.mostrar_productos()
                case "5":
                    break
                case _:
                    print("Opción inválida.")

    # ------------------ MENÚ CLIENTE ------------------
    def menu_cliente(self):
        while True:
            print("\n--- MENÚ CLIENTE ---")
            print("1. Ver productos")
            print("2. Buscar producto")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_productos.mostrar_productos()
                case "2":
                    self.gestion_productos.buscar_producto()
                case "3":
                    break
                case _:
                    print("Opción inválida.")

    # ------------------ MENÚ PROVEEDOR ------------------
    def menu_proveedor(self):
        while True:
            print("\n--- MENÚ PROVEEDOR ---")
            print("1. Registrar proveedor")
            print("2. Ver proveedores")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_proveedores.registrar_proveedor()
                case "2":
                    self.gestion_proveedores.mostrar_proveedores()
                case "3":
                    break
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    gestion_categoria=Gestion_Categorias
    gestion_productos=Gestion_Procudctos(gestion_categoria.categoria)
    gestion_clientes = Gestion_Cliente(OrdenadorProductos())
    gestion_empleados = Gestion_empleado(
        Administrado("admin", "Admin", "123456789", "Direccion", "admin@correo.com", 3000, "admin123"))
    gestion_proveedores = Gestion_Proveedor(gestion_categoria.categoria)
    menu = Menu(gestion_categoria, gestion_productos, gestion_clientes, gestion_empleados, gestion_proveedores)
    menu.mostrar_menu()

