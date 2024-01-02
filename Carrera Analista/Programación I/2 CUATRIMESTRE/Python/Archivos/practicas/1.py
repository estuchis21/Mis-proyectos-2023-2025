nombre_archivo = input("Ingrese el nombre del archivo: ")
cantidad_de_lineas_mostrar = int(input("Ingrese la cantidad de líneas a mostrar: "))

abrir_archivo = open(nombre_archivo, "r") 
lineas = abrir_archivo.readlines()
for i in range(cantidad_de_lineas_mostrar):
    if i < len(lineas):
        print(lineas[i])
    else:
        break


abrir_archivo.close()

