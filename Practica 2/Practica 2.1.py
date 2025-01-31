ventas = [
    {"fecha": "12-01-2023", "producto": "Producto_A", "cantidad": 50, "precio": 45.00, "promocion": True},
    {"fecha": "11-01-2023", "producto": "Producto_AX", "cantidad": 160, "precio": 12.00, "promocion": False},
    {"fecha": "10-01-2023", "producto": "Producto_D", "cantidad": 20, "precio": 15.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_C", "cantidad": 10, "precio": 140.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_D", "cantidad": 1200, "precio": 1.00, "promocion": True}
]

def mostrar_ventas():
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def agregar_producto():
    fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio = float(input("Ingrese el precio del producto: "))
    promocion = input("¿Está en promoción? (s/n): ").strip().lower() == 's'
    ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
    print("Producto agregado correctamente.")

def calcular_suma_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {total:.2f}")

def calcular_promedio_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    promedio = total / len(ventas) if ventas else 0
    print(f"El promedio de ventas es: {promedio:.2f}")

def producto_mas_vendido():
    if not ventas:
        print("No hay ventas registradas.")
        return
    max_producto = max(ventas, key=lambda v: v['cantidad'])
    print(f"El producto con más unidades vendidas es: {max_producto['producto']} con {max_producto['cantidad']} unidades.")

def mostrar_listado_productos():
    productos = {venta['producto'] for venta in ventas}
    print("Listado de productos vendidos:")
    for producto in productos:
        print(f"- {producto}")

def menu():
    while True:
        print("\nMenú de Ventas")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto con más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            calcular_suma_ventas()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_listado_productos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()
