nombre_archivo = input("Ingrese el nombre del archivo: ")
archivo = open(nombre_archivo, "r")
palabra_ingresada = input("Ingrese la palabra: ")
contador_palabra_repetida = 0

for linea in archivo:
    palabras = linea.split()
    contador_palabra_repetida += palabras.count(palabra_ingresada)

archivo.close() 

if contador_palabra_repetida > 0:
    print(f"La palabra '{palabra_ingresada}' se repite {contador_palabra_repetida} veces en el archivo.")
else:
    print(f"La palabra '{palabra_ingresada}' no se encuentra en el archivo.")



    
