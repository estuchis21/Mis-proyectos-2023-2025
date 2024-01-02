import os
# Se abre el archivo en modo lectura
archivo = open("socios.txt", 'r')
edad_preguntar = int(input("Ingrese una edad: "))
encontrado = False

# Se recorre cada línea del archivo
for linea in archivo:
    # Se separan los datos de la línea
    datos_x_separado = linea.strip().split("-")

    # Se compara la edad del socio con la edad ingresada
    if int(datos_x_separado[2]) == edad_preguntar:
        print(f"La info del socio encontrado es: {datos_x_separado[0]}, {datos_x_separado[1]}, {datos_x_separado[3]}")
        encontrado = True

# Se muestra un mensaje si no se encontraron socios con la edad ingresada
if not encontrado:
    print("No se ha encontrado ningún socio con la edad especificada.")

# Se cierra el archivo después de usarlo
archivo.close()
