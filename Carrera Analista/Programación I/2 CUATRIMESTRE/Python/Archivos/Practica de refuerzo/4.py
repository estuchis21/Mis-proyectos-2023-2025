ingreso_archivo_nombre = input("Ingrese el nombre del archivo: ")
expresion = input("Ingrese una frase: ")

abrir_archivo_lectura = open(ingreso_archivo_nombre, 'r')
abrir_archivo_escritura = open("escritura.txt", 'w') 
expresion_encontrada = False

for linea in abrir_archivo_lectura:
    if expresion in linea:
        abrir_archivo_escritura.write(linea)
        expresion_encontrada = True

if expresion_encontrada:
    print("Se ha agregado al archivo 'escritura.txt' las líneas que contienen la expresión.")
else:
    print("No se encontró la expresión en el archivo de lectura.")

abrir_archivo_lectura.close()
abrir_archivo_escritura.close()
