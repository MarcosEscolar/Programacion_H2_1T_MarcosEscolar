
import uuid
clientes = []  
compras = [] 
productos = [
    {"nombre": "Manzana", "precio": 3, "stock": 110},
    {"nombre": "Guisantes", "precio": 2, "stock": 70},
    {"nombre": "Garbanzos", "precio": 1, "stock": 200}
]

# Sirve para introducir los datos de los clientes
def registrar_cliente():
    print("Registrate con los siguientes datos")
    nombre = input("Nombre: ")
    apellidos = input("ingrese al menos un apellido")
    correo = input("Correo electrónico ")
    DNI= input ("ingrese su DNI (campo unico)")


    cliente = {
        "nombre": nombre,
        "apellidos": apellidos,
        "correo": correo,
        "DNI": DNI
    }
    clientes.append(cliente)
    print("Cliente registrado exitosamente.")

# Sirve para ver los clientes registrados
def visualizar_clientes():
    print("Lista de clientes registrados")
    if not clientes:
        print("No hay clientes ren la lista")
    else:
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}, apellidos: {cliente['apellidos']}, DNI: {cliente['DNI']}")

# Sirve para buscar un cliente por DNI
def buscar_cliente():
    print("Buscar Cliente ")
    DNI = input("Introduce tu DNI: ")
    for cliente in clientes:
        if cliente["DNI"] == DNI:
            print(f"Cliente encontrado: Nombre: {cliente['nombre']}, DNI: {cliente['DNI']}")
            return
        else:
            print("El cliente que busca no ha sido encontrado.")

# Sirve para ver los productos en venta
def mostrar_productos():
    print("Productos Disponibles")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

productos = [
    {"nombre": "Manzana", "precio": 3, "stock": 110},
    {"nombre": "Guisantes", "precio": 2, "stock": 70},
    {"nombre": "Garbanzos", "precio": 1, "stock": 200}
]

# Sirve para realizar una compra
def realizar_compra():
    print("Realizar Compra")
    correo = input("Ingrese el DNI del cliente: ")

    # Buscar al cliente
    cliente = next((c for c in clientes if c["correo"] == correo), None)
    if not cliente:
        print("Cliente no encontrado. Registre al cliente antes de realizar una compra.")
        return

    mostrar_productos()

    carrito = []
    while True:
        producto_nombre = input("\nIngrese el nombre del producto a comprar (o 'FIN' para finalizar): ").strip()
        if producto_nombre.upper() == "FIN":
            break

        # Buscar el producto
        producto = next((p for p in productos if p["nombre"] == producto_nombre), None)
        if not producto:
            print("No se ha encontrado rl producto.")
            continue

        # Ver si hay stock del producto
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        if cantidad > producto["stock"]:
            print("No hay disponibl es cantidad.")
            continue

        carrito.append({"producto": producto["nombre"], "cantidad": cantidad})
        producto["stock"] -= cantidad
        print("Producto agregado al carrito.")

    # Registrar la compra
    if carrito:
        numero_pedido = str(uuid.uuid4())
        compras.append({
            "numero_pedido": numero_pedido,
            "cliente": cliente,
            "carrito": carrito,
        })
        print(f"Compra realizada el número de pedido es: {numero_pedido}")
    else:
        print("Para continuar debeb introducir productos en la compra")

# Función para ver el seguimiento de una compra
def seguimiento_compra():
    print("Seguimiento de Compra")
    numero_pedido = int(input("Ingrese el número de pedido: "))

    # Buscar la compra
    compra = next((c for c in compras if c["numero_pedido"] == numero_pedido), None)
    if not compra:
        print("No se ha encontrado su pedido.")
        return

def menu():
    while True:
        print("\n Menú de Pedidos ")
        print("1. Registrar cliente")
        print("2. Visualizar clientes")
        print("3. Buscar cliente")
        print("4. Realizar compra")
        print("5. Seguimiento de compra")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            visualizar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            realizar_compra()
        elif opcion == "5":
            seguimiento_compra()
        elif opcion == "6":
            print("Saliendo del programa. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
