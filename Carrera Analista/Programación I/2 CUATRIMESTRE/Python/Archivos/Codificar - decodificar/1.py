import os
import base64  # Puedes utilizar base64 para codificar y decodificar la información.
def codificar_archivo(nombre_archivo):
    abrir_archivo_original = open(nombre_archivo, 'r')
    contenido = abrir_archivo_original.read()
    contenido_codificado = base64.b64encode(contenido.encode()).decode()
    nombre_archivo_codificado = nombre_archivo.split('.')[0] + "_cod.txt"    
    archivo_codificado = open(nombre_archivo_codificado, 'w')
    archivo_codificado.write(contenido_codificado)               
    print(f'Archivo "{nombre_archivo}" codificado como "{nombre_archivo_codificado}"')
    if not os.path.exists(nombre_archivo):
        print(f'Archivo "{nombre_archivo}" no encontrado.')

def decodificar_archivo(nombre_archivo_codificado):
    archivo_codificado = open(nombre_archivo_codificado, 'r')
    contenido_codificado = archivo_codificado.read()
    contenido_decodificado = base64.b64decode(contenido_codificado).decode()
    nombre_archivo_decodificado = nombre_archivo_codificado.split('_cod.txt')[0] + "_decod.txt"
    archivo_decodificado = open(nombre_archivo_decodificado, 'w')
    archivo_decodificado.write(contenido_decodificado)        
    print(f'Archivo "{nombre_archivo_codificado}" decodificado como "{nombre_archivo_decodificado}"')
    if not os.path.exists(nombre_archivo):
        print(f'Archivo "{nombre_archivo}" no encontrado.')

while True:
    print("Menú:")
    print("1 - Codificar")
    print("2 - Decodificar")
    print("3 - Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre_archivo = input("Ingrese el nombre del archivo a codificar: ")
        codificar_archivo(nombre_archivo)
    elif opcion == "2":
        nombre_archivo_codificado = input("Ingrese el nombre del archivo codificado: ")
        decodificar_archivo(nombre_archivo_codificado)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")