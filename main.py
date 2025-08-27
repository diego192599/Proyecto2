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
            return True
        elif tipo == 'venta':
            if self.stock >= cantidad:
                self.stock -= cantidad
                self.total_ventas += cantidad
                return True
            else:
                print("Error: No hay suficiente stock para la venta.")
                return False
        return False

    def mostrar_info(self):
        return f"[{self.codigo_producto}] {self.nombre} | Precio: {self.precio:.2f} | Stock: {self.stock}"


class Gestion_Productos:
    def __init__(self, categorias):
        self.productos = {}
        self.categorias = categorias
        self.limite_stock=None
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.split()
                    if linea:
                        codigo, id_categoria, nombre, precio, stock = linea.split(",")
                        self.productos[codigo] = {
                            "id_categoria": id_categoria,
                            "nombre": nombre,
                            "precio": float(precio),
                            "stock": int(stock)
                        }
            print("Productos importados desde productos.txt")
        except FileNotFoundError:
         print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for codigo, datos in self.productos.items():
                archivo.write(
                    f"{codigo},{datos['id_categoria']},{datos['nombre']},{datos['precio']},{datos['stock']}\n")

    def agregar_producto(self):
        contador = 0
        while True:
            contador += 1
            print(f"\n--- Agregar Producto {contador} ---")

            codigo_producto = input("Código del producto: ")
            id_categoria = input("ID de categoría: ")

            if id_categoria not in self.categorias.categorias:
                print("Error: La categoría no existe. Agrega primero la categoría.")
                continue

            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
            except ValueError:
                print("Precio inválido. Inténtelo de nuevo.")
                continue

            stock = 0

            self.productos[codigo_producto] = {
                "id_categoria": id_categoria,
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }

            self.guardar_productos()
            print(f"Producto '{nombre}' agregado y guardado correctamente con stock inicial {stock}.")

            continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
            if continuar != 's':
                print(f"Se agregaron {contador} producto(s) en total.")
                break

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        for p in self.productos.values():
            categoria = self.categorias.categorias[p.id_categoria]
            print(f"[{p.codigo_producto}] {p.nombre} | Precio: {p.precio:.2f} | Categoría: {categoria.nombre} | Stock: {p.stock}")

    def eliminar_producto(self):
        if not self.productos:
            print("No hay productos.")
            return
        print("1. Eliminar por código")
        print("2. Eliminar por stock máximo")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            codigo = input("Ingrese el código a eliminar: ")
            if codigo in self.productos:
                del self.productos[codigo]
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        elif opcion == "2":
            eliminar_lista = [codigo for codigo, prod in self.productos.items()
                              if prod.stock > Gestion_Productos.limite_stock]
            for codigo in eliminar_lista:
                del self.productos[codigo]
            print(f"{len(eliminar_lista)} productos eliminados correctamente.")
        else:
            print("Opción no válida.")

    def buscar_producto(self):
        if not self.productos:
            print("No hay productos.")
            return
        criterio = input("Ingrese el nombre o código del producto a buscar: ").lower()
        encontrados = [p for p in self.productos.values()
                       if criterio in p.nombre.lower() or criterio == p.codigo_producto]
        if encontrados:
            for prod in encontrados:
                print(f"[{prod.codigo_producto}] {prod.nombre} - Stock: {prod.stock}")
        else:
            print("Productos no encontrados.")

    def ordenar_productos(self, ordenador):
        if not self.productos:
            print("No hay productos para ordenar.")
            return

        print("\n--- ORDENAR PRODUCTOS ---")
        print("1. Por nombre")
        print("2. Por precio")
        print("3. Por cantidad")
        print("4. Por código")
        opcion = input("Seleccione una opción: ")

        criterios = {"1": "nombre", "2": "precio", "3": "stock", "4": "codigo_producto"}
        criterio = criterios.get(opcion)
        if not criterio:
            print("Opción inválida.")
            return

        lista_productos = list(self.productos.values())
        ordenados = ordenador.quicksort(lista_productos, criterio)

        for p in ordenados:
            print(f"[{p.codigo_producto}] {p.nombre} | Precio: {p.precio:.2f} | Stock: {p.stock}")


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
            elif criterio == "codigo_producto":
                menores = [x for x in lista[1:] if x.codigo_producto <= pivote.codigo_producto]
                mayores = [x for x in lista[1:] if x.codigo_producto > pivote.codigo_producto]
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
    def __init__(self, id_cliente, nombre, telefono, correo, direccion="", total_compras=0, descuento=0):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.total_compras = total_compras
        self.descuento = descuento

    def mostrar_info(self):
        return f"[{self.id_cliente}] {self.nombre} | Compras: {self.total_compras} | Descuento: {self.descuento}%"


class Gestion_Cliente:
    def __init__(self, ordenador):
        self.clientes = {}
        self.cargar_clientes()
        self.ordenador = ordenador

    def cargar_clientes(self):
        try:
            with open("clientes.txt","r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        self.clientes[nit] = Cliente(
                            id_cliente=nit,
                            nombre=nombre,
                            telefono=telefono,
                            correo=correo,
                            direccion=direccion
                        )
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_cliente(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, cliente in self.clientes.items():
                archivo.write(f"{cliente.id_cliente}:{cliente.nombre}:{cliente.direccion}:{cliente.telefono}:{cliente.correo}\n")

    def agregar_cliente(self, nit, nombre, direccion, telefono, correo):
        self.clientes[nit] = Cliente(nit, nombre, telefono, correo, direccion)
        self.guardar_cliente()
        print(f"Cliente con NIT {nit} se agregó y guardó correctamente.")

    def asignar_descuento(self, nit, porcentaje):
        if nit in self.clientes:
            try:
                self.clientes[nit].descuento = float(porcentaje)
                print(f"Descuento de {porcentaje}% asignado a {self.clientes[nit].nombre}.")
            except ValueError:
                print("Porcentaje de descuento inválido.")
        else:
            print("Cliente no encontrado.")

    def listar_ordenados_por_compras(self):
        lista_clientes = list(self.clientes.values())
        if not lista_clientes:
            print("No hay clientes para ordenar.")
            return
        ordenados = self.ordenador.quicksort_clientes(lista_clientes)
        for c in ordenados:
            print(f"{c.nombre} - Compras: {c.total_compras} - Descuento: {c.descuento}%")

    def mostrar_todos(self):
        if self.clientes:
            print("\nLista de clientes:")
            for nit, cliente in self.clientes.items():
                print(cliente.mostrar_info())
        else:
            print("No hay clientes registrados.")

    def buscar_clientes(self):
        criterio = input("Ingrese el nombre o ID del cliente: ").lower()
        encontrados = [c for c in self.clientes.values()
                       if criterio in c.nombre.lower() or criterio == c.id_cliente]
        if encontrados:
            for c in encontrados:
                print(c.mostrar_info())
        else:
            print("Cliente no encontrado.")


class Empleado:
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


class Administrador(Empleado):
    def __init__(self, id_empleado, nombre, telefono, direccion, correo, salario_base, password):
        super().__init__(id_empleado, nombre, telefono, direccion, correo, salario_base)
        self.password = password

    def verificar_password(self, password_ingresada):
        print("Verificando si usted es administrador...")
        return self.password == password_ingresada


class Gestion_empleado:
    def __init__(self, admin):
        self.empleados = {}
        self.admin = admin

    def agregar_empleado(self, password_admin):
        if not self.admin.verificar_password(password_admin):
            print("Solo el Administrador puede agregar empleados.")
            return
        print("\n---Agregar Empleado---")
        id_empleado = input("Ingrese la ID del nuevo empleado: ")
        nombre = input("Nombre del empleado: ")
        telefono = input("El número que nos servirá para contactarlo: ")
        direccion = input("Ingrese la dirección: ")
        correo = input("Ingrese el correo personal del empleado: ")
        try:
            salario_base = float(input("Ingrese el salario que recibirá el empleado: "))
        except ValueError:
            print("Salario inválido. Inténtelo de nuevo.")
            return

        nuevo_empleado = Empleado(id_empleado, nombre, telefono, direccion, correo, salario_base)
        self.empleados[id_empleado] = nuevo_empleado
        print(f"Empleado {nombre} agregado correctamente.")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return
        for e in self.empleados.values():
            print(e.mostrar_info())

    def buscar_empleado(self):
        criterio = input("Ingrese el ID o nombre: ").lower()
        encontrados = [e for e in self.empleados.values()
                       if criterio in e.nombre.lower() or criterio == e.id_empleado]
        if encontrados:
            for e in encontrados:
                print(e.mostrar_info())
        else:
            print("Empleado no encontrado.")

    def despedir_empleado(self):
        id_empleado = input("Ingrese el ID del empleado a despedir: ")
        if id_empleado in self.empleados:
            empleado_despedido = self.empleados.pop(id_empleado)
            print(f"Empleado {empleado_despedido.nombre} ha sido despedido.")
        else:
            print("No hay ningún empleado con ese ID.")


class Proveedor:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria

    def mostrar_info(self, categorias):
        categoria_nombre = categorias.categorias[self.id_categoria].nombre
        return f"[{self.id_proveedor}] {self.nombre} ({self.empresa}) - Categoría: {categoria_nombre}"


class Gestion_Proveedor:
    def __init__(self, categorias):
        self.proveedores = {}
        self.categorias = categorias

    def agregar_proveedor(self):
        id_proveedor = input("Ingrese el ID del proveedor: ")
        if id_proveedor in self.proveedores:
            print("El proveedor ya fue registrado.")
            return
        nombre = input("Ingrese el nombre: ")
        empresa = input("Ingrese la empresa: ")
        telefono = input("Teléfono: ")
        direccion = input("Ingrese la dirección: ")
        correo = input("Ingrese el correo de la empresa: ")
        id_categoria = input("Ingrese la ID de la categoría: ")
        if id_categoria not in self.categorias.categorias:
            print("La categoría no existe.")
            return

        self.proveedores[id_proveedor] = Proveedor(id_proveedor, nombre, empresa, telefono, direccion, correo,
                                                   id_categoria)
        print("Se agregó correctamente el proveedor.")

    def mostrar_proveedores(self):
        if not self.proveedores:
            print("No hay proveedores registrados.")
            return
        for p in self.proveedores.values():
            print(p.mostrar_info(self.categorias))


class DetalleVenta:
    def __init__(self, id_detalle, id_venta, codigo_producto, cantidad, precio):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.cantidad * self.precio


class Venta:
    def __init__(self, id_venta, fecha, id_cliente, id_empleado):
        self.id_venta = id_venta
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        return sum(d.subtotal for d in self.detalles)


class Compra:
    def __init__(self, id_compra, fecha, id_proveedor, id_empleado):
        self.id_compra = id_compra
        self.fecha = fecha
        self.id_proveedor = id_proveedor
        self.id_empleado = id_empleado
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        return sum(d.subtotal for d in self.detalles)


class DetalleCompra:
    def __init__(self, id_detalle, id_compra, codigo_producto, cantidad, precio_compra, fecha_caducidad):
        self.id_detalle = id_detalle
        self.id_compra = id_compra
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.fecha_caducidad = fecha_caducidad
        self.subtotal = cantidad * precio_compra


class Gestion_Venta:
    def __init__(self, productos, clientes, empleados):
        self.ventas = {}
        self.productos = productos
        self.clientes = clientes
        self.empleados = empleados

    def registrar_venta(self):
        id_venta = input("ID de la venta: ")
        fecha = input("Fecha de la venta (YYYY-MM-DD): ")
        id_cliente = input("ID del cliente: ")
        id_empleado = input("ID del empleado: ")

        if id_cliente not in self.clientes.clientes:
            print("Cliente no encontrado. Debe registrarlo primero.")
            return
        if id_empleado not in self.empleados.empleados:
            print("Empleado no encontrado.")
            return

        venta = Venta(id_venta, fecha, id_cliente, id_empleado)
        total_venta = 0

        while True:
            codigo_producto = input("Código del producto (o 'fin' para terminar): ")
            if codigo_producto.lower() == 'fin':
                break
            if codigo_producto not in self.productos.productos:
                print("Producto no encontrado.")
                continue

            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida.")
                continue

            producto = self.productos.productos[codigo_producto]
            if not producto.actualizar_stock(cantidad, 'venta'):
                continue

            precio_venta = producto.precio
            detalle = DetalleVenta(
                id_detalle=len(venta.detalles) + 1,
                id_venta=id_venta,
                codigo_producto=codigo_producto,
                cantidad=cantidad,
                precio=precio_venta
            )
            venta.agregar_detalle(detalle)
            total_venta += detalle.subtotal

        self.ventas[id_venta] = venta
        print(f"Venta registrada. Total: {total_venta:.2f}")


class Gestion_Compra:
    def __init__(self, productos, proveedores):
        self.compras = {}
        self.productos = productos
        self.proveedores = proveedores

    def registrar_compra(self):
        id_compra = input("ID de la compra: ")
        fecha = input("Fecha de la compra (YYYY-MM-DD): ")
        id_proveedor = input("Ingrese ID del proveedor: ")
        id_empleado = input("Ingrese ID del empleado: ")

        if id_proveedor not in self.proveedores.proveedores:
            print("No existe ese proveedor.")
            return

        compra = Compra(id_compra, fecha, id_proveedor, id_empleado)
        total_compra = 0

        while True:
            codigo_producto = input("Código del producto (o 'fin' para terminar): ")
            if codigo_producto.lower() == 'fin':
                break
            if codigo_producto not in self.productos.productos:
                print("Producto no encontrado.")
                continue

            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio de compra: "))
            except ValueError:
                print("Valores inválidos. Inténtelo de nuevo.")
                continue

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
            producto = self.productos.productos[codigo_producto]
            producto.actualizar_stock(cantidad, 'compra')
            total_compra += detalle.subtotal

        self.compras[id_compra] = compra
        print(f"Compra registrada. Total: {total_compra:.2f}")


class Gestion_Categoria:
    def __init__(self):
        self.categorias = {}

    def agregar_categoria(self):
        id_categoria = input("Ingrese el ID de la categoría: ")
        nombre = input("Ingrese el nombre de la categoría: ")
        self.categorias[id_categoria] = Categorias(id_categoria, nombre)
        print(f"Categoría '{nombre}' agregada correctamente.")

    def mostrar_categorias(self):
        if not self.categorias:
            print("No hay categorías registradas.")
            return
        print("\n--- CATEGORÍAS REGISTRADAS ---")
        for cat in self.categorias.values():
            print(f"[{cat.id_categoria}] {cat.nombre}")


class Menu:
    def __init__(self):
        self.ordenador = OrdenadorProductos()
        self.admin = Administrador("admin", "Admin", "N/A", "N/A", "admin@farmacia.com", 1000, "admin123")

        self.gestion_categorias = Gestion_Categoria()
        self.gestion_productos = Gestion_Productos(self.gestion_categorias)
        self.gestion_clientes = Gestion_Cliente(self.ordenador)
        self.gestion_empleados = Gestion_empleado(self.admin)
        self.gestion_proveedores = Gestion_Proveedor(self.gestion_categorias)
        self.gestion_compras = Gestion_Compra(self.gestion_productos, self.gestion_proveedores)
        self.gestion_ventas = Gestion_Venta(self.gestion_productos, self.gestion_clientes, self.gestion_empleados)

    def mostrar_menu(self):
        while True:
            print("\n=== SISTEMA DE FARMACIA ===")
            print("1. Menú Administrador")
            print("2. Menú Empleado")
            print("3. Menú Cliente")
            print("4. Menú Proveedor")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_admin()
            elif opcion == "2":
                self.menu_empleado()
            elif opcion == "3":
                self.menu_cliente()
            elif opcion == "4":
                self.menu_proveedor()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

    def menu_admin(self):
        clave = input("Ingrese la contraseña de administrador: ")
        if not self.admin.verificar_password(clave):
            print("Contraseña incorrecta.")
            return

        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Gestionar categorías")
            print("2. Gestionar productos")
            print("3. Gestionar empleados")
            print("4. Gestionar proveedores")
            print("5. Ver compras registradas")
            print("6. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_gestionar_categorias()
            elif opcion == "2":
                self.menu_gestionar_productos_admin()
            elif opcion == "3":
                self.menu_gestionar_empleados()
            elif opcion == "4":
                self.menu_gestionar_proveedores()
            elif opcion == "5":
                print("Compras registradas: ")
                # Lógica para mostrar compras
            elif opcion == "6":
                break
            else:
                print("Opción inválida.")

    def menu_gestionar_categorias(self):
        while True:
            print("\n--- GESTIÓN DE CATEGORÍAS ---")
            print("1. Agregar categoría")
            print("2. Mostrar categorías")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_categorias.agregar_categoria()
            elif opcion == "2":
                self.gestion_categorias.mostrar_categorias()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")

    def menu_gestionar_productos_admin(self):
        while True:
            print("\n--- GESTIÓN DE PRODUCTOS ---")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Eliminar producto")
            print("4. Buscar producto")
            print("5. Ordenar productos")
            print("6. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_productos.agregar_producto()
            elif opcion == "2":
                self.gestion_productos.mostrar_productos()
            elif opcion == "3":
                self.gestion_productos.eliminar_producto()
            elif opcion == "4":
                self.gestion_productos.buscar_producto()
            elif opcion == "5":
                self.gestion_productos.ordenar_productos(self.ordenador)
            elif opcion == "6":
                break
            else:
                print("Opción inválida.")

    def menu_gestionar_empleados(self):
        while True:
            print("\n--- GESTIÓN DE EMPLEADOS ---")
            print("1. Agregar empleado")
            print("2. Mostrar empleados")
            print("3. Buscar empleado")
            print("4. Despedir empleado")
            print("5. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_empleados.agregar_empleado("admin123")
            elif opcion == "2":
                self.gestion_empleados.mostrar_empleados()
            elif opcion == "3":
                self.gestion_empleados.buscar_empleado()
            elif opcion == "4":
                self.gestion_empleados.despedir_empleado()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")

    def menu_gestionar_proveedores(self):
        while True:
            print("\n--- GESTIÓN DE PROVEEDORES ---")
            print("1. Agregar proveedor")
            print("2. Mostrar proveedores")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_proveedores.agregar_proveedor()
            elif opcion == "2":
                self.gestion_proveedores.mostrar_proveedores()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")

    def menu_empleado(self):
        while True:
            print("\n--- MENÚ EMPLEADO ---")
            print("1. Registrar venta")
            print("2. Registrar compra")
            print("3. Ver productos")
            print("4. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_ventas.registrar_venta()
            elif opcion == "2":
                self.gestion_compras.registrar_compra()
            elif opcion == "3":
                self.gestion_productos.mostrar_productos()
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    def menu_cliente(self):
        while True:
            print("\n--- MENÚ DE CLIENTES ---")
            print("1. Agregar cliente")
            print("2. Mostrar todos los clientes")
            print("3. Buscar cliente")
            print("4. Asignar descuento a cliente")
            print("5. Listar clientes ordenados por compras")
            print("6. Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                nit = input("NIT: ")
                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                telefono = input("Teléfono: ")
                correo = input("Correo: ")
                self.gestion_clientes.agregar_cliente(nit, nombre, direccion, telefono, correo)

            elif opcion == "2":
                self.gestion_clientes.mostrar_todos()

            elif opcion == "3":
                self.gestion_clientes.buscar_clientes()

            elif opcion == "4":
                nit = input("Ingrese NIT del cliente: ")
                porcentaje = input("Ingrese porcentaje de descuento: ")
                self.gestion_clientes.asignar_descuento(nit, porcentaje)

            elif opcion == "5":
                self.gestion_clientes.listar_ordenados_por_compras()

            elif opcion == "6":
                print("Regresando al menú principal...")
                break

            else:
                print("Opción inválida, intenta de nuevo.")

    def menu_proveedor(self):
        while True:
            print("\n--- MENÚ PROVEEDOR ---")
            print("1. Registrar proveedor")
            print("2. Ver proveedores")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.gestion_proveedores.agregar_proveedor()
            elif opcion == "2":
                self.gestion_proveedores.mostrar_proveedores()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    app = Menu()
    app.mostrar_menu()