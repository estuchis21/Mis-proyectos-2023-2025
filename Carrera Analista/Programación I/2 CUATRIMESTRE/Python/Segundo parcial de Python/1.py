import os
alumnos = {}
def ingreso_alumnos():
    for i in range(5):
        nombre_carrera = input("Ingrese el nombre de la carrera al que se inscribe: ")
        cantidad = int(input("Ingrese la cantidad de alumnos en cada carrera: "))
        alumnos[nombre_carrera] = cantidad
    return alumnos

def calculo_promedios():
    suma = 0
    for cantidad in alumnos.values():
        suma += cantidad
    contador = len(alumnos)
    promedio = suma / contador
    # ahora escribir en un archivo, el promedio obtenido
    abrir_archivo = open('resultado.txt', 'w')
    abrir_archivo.write(f"El promedio de inscriptos entre las 5 carreras es de {promedio} alumnos.")

# Primero ingresamos los datos de los alumnos
ingreso_alumnos()

# Luego calculamos y escribimos el promedio
calculo_promedios()

