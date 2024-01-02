import os
def suma_y_promedio():
    abrir_archivo = open("requerimientos.txt", "r")
    suma = 0
    contador = 0
    for linea in abrir_archivo:
        mes, requerimientos = linea.strip().split("=")
        requerimientos_int = int(requerimientos)
        suma += requerimientos_int
        contador += 1
    if contador == 0:
        return 0, 0  # Avoid division by zero if the file is empty
    promedio = suma / contador
    return suma, promedio

def mayor():
    abrir_archivo = open("requerimientos.txt", "r")
    mayor_requerimientos = 0
    mes_mayor_requerimientos = ""
    for linea in abrir_archivo:
        mes, requerimientos = linea.strip().split("=")
        requerimientos_int = int(requerimientos)
        if requerimientos_int > mayor_requerimientos:
            mayor_requerimientos = requerimientos_int
            mes_mayor_requerimientos = mes
    return mes_mayor_requerimientos

total_requerimientos, promedio_requerimientos = suma_y_promedio()
print(f"Se ha ahorrado un total de requerimientos de: {total_requerimientos}")
print(f"El mes con mayor requerimientos es {mayor()}")
print(f"El promedio de requerimientos es: {promedio_requerimientos}")
