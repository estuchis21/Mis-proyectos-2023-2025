#abrir el archivo juegos.txt, que contiene una lista de los juegos mas populares y su cantidad de descargas. Recorrer ese archivo e imprimir el juego mas descargado
import os
# Abre el archivo en modo lectura
abrir_archivo = open('juegos.txt', 'r')
# Inicializa variables para almacenar el juego más descargado
juego_mas_descargado = ''
descargas_mas_altas = 0

# Recorre cada línea del archivo
for linea in abrir_archivo:
    # Divide la línea en nombre del juego y cantidad de descargas
    juego, descargas_str = linea.strip().split(' ')
        
    # Convierte la cantidad de descargas a un número entero
    descargas = int(descargas_str)
        
    # Comprueba si la cantidad de descargas es mayor que la actual más alta
    if descargas > descargas_mas_altas:
        descargas_mas_altas = descargas
        juego_mas_descargado = juego

# Imprime el juego más descargado
print(f"El juego más descargado es: {juego_mas_descargado} con {descargas_mas_altas} descargas.")
# Cierra el archivo
abrir_archivo.close()
