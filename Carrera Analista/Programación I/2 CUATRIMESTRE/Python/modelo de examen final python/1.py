import os
# primera funcion: rubro que mas vendio
def may_ventas():
    abrir_archivo = open("ventas.txt", "r")
    mayor_venta_num = 0
    rubro_mayor_ventas = ''
    for linea in abrir_archivo:
        rubro, ventas_str = linea.strip().split("=")
        #pasamos a numero entero las ventas
        ventas = int(ventas_str)
        #mayor rubro de ventas
        if ventas > mayor_venta_num:
            mayor_venta_num = ventas
            rubro_mayor_ventas = rubro
    return rubro_mayor_ventas

# segunda funcion: promedio de ventas por rubro
def promedio():
    abrir_archivo = open("ventas.txt", "r") 
    total_ventas = 0
    contador = 0
    for linea in abrir_archivo:
        rubro, ventas_str = linea.strip().split("=")
        ventas = int(ventas_str)
        total_ventas += ventas
        contador +=1
    promedio_ventas = total_ventas/contador
    return promedio_ventas

print(f"El rubro con mayor ventas es: {may_ventas()}")
print(f"El promedio de las ventas generales es de: {promedio()}")


