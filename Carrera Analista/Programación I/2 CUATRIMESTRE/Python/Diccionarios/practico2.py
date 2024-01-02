# Función para ingresar productos y sus valores
def ingreso_producto(productos):
    producto = input("Ingrese el nombre del producto tecnológico: ")
    valor_producto = int(input("Ingrese el valor del producto: "))
    productos[producto] = valor_producto

# Función para mostrar todos los productos con sus valores
def mostrar_todo(productos):
    print("Mostrar productos con sus respectivos valores: ")
    for producto, valor_producto in productos.items():
        print(f"Producto: {producto}, con su valor: {valor_producto}")

# Función para calcular el promedio de los valores de los productos
def calcular_promedio(productos):
    suma = sum(productos.values())  # Sumar los valores de los productos
    promedio = suma / len(productos)
    return promedio

def mayor_precio(productos):
    max_valor = max(productos.values())
    producto_mayor_precio = [producto for producto, valor in productos.items() if valor == max_valor]
    return producto_mayor_precio

def menor_precio(productos):
    min_valor = min(productos.values())
    producto_menor_valor = [producto for producto, valor in productos.items() if valor == min_valor]
    return producto_menor_valor


# Función principal
def main():
    productos = {}
    cantidad_de_items = int(input("Ingrese la cantidad de productos que desea agregar: "))
    for i in range(cantidad_de_items):
        print(f"Ingrese los datos del producto {i + 1}: ")
        ingreso_producto(productos)
        mostrar_todo(productos)
    # Calcular y mostrar el promedio
    promedio_valor = calcular_promedio(productos)
    print(f"El promedio de los valores de los productos es: {promedio_valor}")
    # Mostrar el mayor venta
    productos_mayor_precio = mayor_precio(productos)
    if len(productos_mayor_precio) == 1:
        print(f"El producto con el mayor precio es: {productos_mayor_precio[0]}")
    else:
        print(f"Los productos con el mayor precio son: {', '.join(productos_mayor_precio)}")

    # Mostrar el menor venta

    productos_menor_precio = menor_precio(productos)
    if len(productos_menor_precio) == 1:
        print(f"El producto con el mayor precio es: {productos_menor_precio[0]}")
    else:
        print(f"Los productos con el mayor precio son: {', '.join(productos_menor_precio)}")

if __name__ == "__main__":
    main()











