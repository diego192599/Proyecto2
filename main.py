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


class Gestion_Productos:
    contador = 0
    limite_Stock = 50

    def __init__(self, categorias):
        self.productos = {}
        self.categorias = categorias

    def agregar_producto(self):
        while True:
            Gestion_Productos.contador += 1
            print(f"\n--- Agregar Producto {Gestion_Productos.contador} ---")

            codigo_producto = input("Código del producto: ")
            id_categoria = input("ID de categoría: ")

            if id_categoria not in self.categorias:
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
            categorias = self.categorias[p.id_categoria]
            print(f"[{p.codigo_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {categorias.nombre} | Stock: {p.stock}")

    def eliminar(self):
        if not self.productos:
            print("No hay productos")
            return
        print("1. Eliminar por código")
        print("2. Eliminar por máximo de stock")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            codigo = input("Ingrese el código a eliminar: ")
            if codigo in self.productos:
                del self.productos[codigo]
                print("Producto eliminado")
            else:
                print("Producto no encontrado")
        elif opcion == "2":
            eliminar = [codigo for codigo, prod in self.productos.items()
                        if prod.stock > Gestion_Productos.limite_Stock]
            for codigo in eliminar:
                del self.productos[codigo]
            print(f"{len(eliminar)} productos eliminados correctamente")
        else:
            print("Opción no válida")

    def buscar(self):
        if not self.productos:
            print("No hay productos")
            return
        criterio = input("Ingrese el nombre o código del producto a buscar: ").lower()
        encontrados = [p for p in self.productos.values()
                       if criterio in p.nombre.lower() or criterio == p.codigo_producto]
        if encontrados:
            for prod in encontrados:
                print(f"{prod.codigo_producto} - {prod.nombre} - Stock: {prod.stock}")
        else:
            print("Productos no encontrados")


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
            else:
                return lista

            return self.quicksort(menores, criterio) + [pivote] + self.quicksort(mayores, criterio)


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

    def agregar_cliente(self):
        id_cliente = input("Ingrese el ID del cliente: ")
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico personal: ")
        self.clientes[id_cliente] = Cliente(id_cliente, nombre, correo)
        print(f"El cliente {nombre} se agregó correctamente")

    def listar_ordenados_por_compras(self):
        lista_clientes = list(self.clientes.values())
        ordenados = self.ordenador.quicksort(lista_clientes, "total_compras")
        for c in ordenados:
            print(f"{c.nombre} - Compras: {c.total_compras} - Descuento: {c.descuento}%")

    def mostrar(self):
        if not self.clientes:
            print("No hay clientes")
            return
        for c in self.clientes.values():
            print(f"{c.id_cliente} - {c.nombre} - {c.correo}")

    def buscar_clientes(self):
        criterio = input("Ingrese el nombre o ID del cliente: ").lower()
        encontrados = [c for c in self.clientes.values()
                       if criterio in c.nombre.lower() or criterio == c.id_cliente]
        if encontrados:
            for c in encontrados:
                print(f"{c.id_cliente} - {c.nombre} - {c.correo}")
        else:
            print("Cliente no encontrado")


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
        return f"{self.id_empleado} - {self.nombre} - Salario: {self.calcular_salario():.2f}"


class Administrador(Empleado):
    def __init__(self, id_empleado, nombre, telefono, direccion, correo, salario_base, password):
        super().__init__(id_empleado, nombre, telefono, direccion, correo, salario_base)
        self.password = password

    def verificar_password(self, password_ingresada):
        return self.password == password_ingresada


class Gestion_Empleado:
    contador = 0

    def __init__(self, admin):
        self.empleados = {}
        self.admin = admin

    def agregar_empleado(self):
        password = input("Ingrese la contraseña de administrador: ")
        if not self.admin.verificar_password(password):
            print("Solo el Administrador puede agregar empleados")
            return
        Gestion_Empleado.contador += 1
        print(f"\n--- Agregar Empleado {Gestion_Empleado.contador} ---")
        id_empleado = input("Ingrese la ID del nuevo empleado: ")
        nombre = input("Nombre del empleado: ")
        telefono = input("El número que nos servirá para contactarlo: ")
        direccion = input("Ingrese la dirección: ")
        correo = input("Ingrese el correo personal del empleado: ")
        salario_base = float(input("Ingrese el salario que recibirá el empleado: "))
        nuevo = Empleado(id_empleado, nombre, telefono, direccion, correo, salario_base)
        self.empleados[id_empleado] = nuevo
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


class Proveedor:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria


class Gestion_Proveedor:
    def __init__(self, categorias):
        self.proveedores = {}
        self.categorias = categorias

    def agregar(self):
        id_proveedor = input("Ingrese el ID del proveedor: ")
        if id_proveedor in self.proveedores:
            print("El proveedor ya fue registrado")
            return
        nombre = input("Ingrese el nombre: ")
        empresa = input("Ingrese la empresa de la cual viene: ")
        telefono = input("Teléfono: ")
        direccion = input("Ingrese la dirección de donde proviene: ")
        correo = input("Ingrese el correo de la empresa: ")
        id_categoria = input("Ingrese la ID de la categoría: ")
        if id_categoria not in self.categorias:
            print("La categoría no existe")
            return
        self.proveedores[id_proveedor] = Proveedor(id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria)
        print("Proveedor agregado correctamente")

    def listar(self):
        if not self.proveedores:
            print("No hay proveedores")
            return
        for p in self.proveedores.values():
            cat = self.categorias[p.id_categoria].nombre
            print(f"[{p.id_proveedor}] {p.nombre} ({p.empresa}) - Categoría: {cat}")


class Menu:
    def __init__(self, gestion_categorias, gestion_productos, gestion_clientes, gestion_empleados, gestion_proveedores):
        self.gestion_categorias = gestion_categorias
        self.gestion_productos = gestion_productos
        self.gestion_clientes = gestion_clientes
        self.gestion_empleados = gestion_empleados
        self.gestion_proveedores = gestion_proveedores

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
                    return
                case _:
                    print("Opción inválida.")

    def menu_admin(self):
        clave = input("Ingrese la contraseña de administrador: ")
        if clave != "admin123":
            print("Contraseña incorrecta.")
            return

        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Gestionar categorías")
            print("2. Gestionar productos")
            print("3. Gestionar empleados")
            print("4. Gestionar proveedores")
            print("5. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_categorias.agregar_categoria()
                case "2":
                    self.gestion_productos.agregar_producto()
                case "3":
                    self.gestion_empleados.agregar_empleado()
                case "4":
                    self.gestion_proveedores.agregar()
                case "5":
                    break
                case _:
                    print("Opción inválida.")

    def menu_empleado(self):
        while True:
            print("\n--- MENÚ EMPLEADO ---")
            print("1. Ver productos")
            print("2. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_productos.mostrar_info()
                case "2":
                    break
                case _:
                    print("Opción inválida.")

    def menu_cliente(self):
        while True:
            print("\n--- MENÚ CLIENTE ---")
            print("1. Ver productos")
            print("2. Buscar producto")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_productos.mostrar_info()
                case "2":
                    self.gestion_productos.buscar()
                case "3":
                    break
                case _:
                    print("Opción inválida.")

    def menu_proveedor(self):
        while True:
            print("\n--- MENÚ PROVEEDOR ---")
            print("1. Registrar proveedor")
            print("2. Ver proveedores")
            print("3. Volver")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.gestion_proveedores.agregar()
                case "2":
                    self.gestion_proveedores.listar()
                case "3":
                    break
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    gestion_categorias = Gestion_Categorias()
    gestion_productos = Gestion_Productos(gestion_categorias.categorias)
    gestion_clientes = Gestion_Cliente(OrdenadorProductos())
    gestion_empleados = Gestion_Empleado(Administrador("admin", "Admin", "123456789", "Direccion", "admin@correo.com", 3000, "admin123"))
    gestion_proveedores = Gestion_Proveedor(gestion_categorias.categorias)

    menu = Menu(gestion_categorias, gestion_productos, gestion_clientes, gestion_empleados, gestion_proveedores)
    menu.mostrar_menu()
