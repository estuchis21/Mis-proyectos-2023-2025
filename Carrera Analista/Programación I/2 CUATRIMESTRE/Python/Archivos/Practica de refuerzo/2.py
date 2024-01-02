# Escribir un programa, que solicite al usuario el nombre de un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

nombre_de_archivo_ingreso = input("Ingrese el nombre del archivo: ")
archivo = open(nombre_de_archivo_ingreso, "r")
contador_lineas = 0
contador_palabras = 0
contador_caracteres = 0
#cantidad de líneas, palabras y caracteres

for linea in archivo:
    contador_lineas += 1
    palabras = linea.split()
    contador_palabras += len(palabras)
    contador_caracteres += len(linea)

print("Número de líneas:", contador_lineas)
print("Número de palabras:", contador_palabras)
print("Número de caracteres:", contador_caracteres)





