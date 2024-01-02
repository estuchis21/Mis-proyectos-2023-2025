import os
def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    
    existe = False
    
    archivo_lectura = open("agenda.txt", "r")
    for linea in archivo_lectura:
        contacto = linea.strip().split(":")
        if nombre == contacto[0] or telefono == contacto[1]:
            print("El contacto ya existe en la agenda.")
            existe = True
            break
    
    if not existe:
        archivo_escritura = open("agenda.txt", "w")
        archivo_escritura.write(f"{nombre}:{telefono}\n")
        print("Contacto agregado correctamente.")

def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    contactos = {}
    archivo_lectura = open("agenda.txt", "r")
    for linea in archivo_lectura:
        nombre, telefono = linea.strip().split(":")
        contactos[nombre] = telefono
    
    if nombre_buscar in contactos:
        print(f"Teléfono de {nombre_buscar}: {contactos[nombre_buscar]}")
    else:
        print(f"{nombre_buscar} no se encuentra en la agenda.")
        agregar = input("¿Desea agregar este contacto? (S/N): ").upper()
        if agregar == "S":
            telefono = input("Ingrese el teléfono: ")
            archivo_escritura = open("agenda.txt", "w")
            archivo_escritura.write(f"{nombre_buscar}:{telefono}\n")
            print(f"Contacto {nombre_buscar} agregado correctamente.")
        else:
            print("No se agregó el contacto.")

while True:
    print("Menú de la Agenda:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        print("Hasta luego. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")