import os
while True:
    print("1. Log in")
    print("2. Salir")
    opcion = int(input("Ingrese la opción elegida: "))

    if opcion == 1:
        dni = input("Ingrese su DNI: ")
        clave = input("Ingrese su clave: ")
        abrir_archivo = open("2 CUATRIMESTRE\\Archivos\\usuarios.txt", "r")
        nombre = ""
        for linea in abrir_archivo:
            datos_por_separado = linea.strip().split("-")
            if len(datos_por_separado) == 3 and datos_por_separado[1] == dni and datos_por_separado[2] == clave:
                nombre = datos_por_separado[0]
                break
        abrir_archivo.close()
        
        if nombre == "":
            print("Usuario no encontrado")
        else:
            print("Bienvenidx al sistema, ", nombre)
    elif opcion == 2:
        break
    else:
        print("Ingrese opciones 1 o 2.")


