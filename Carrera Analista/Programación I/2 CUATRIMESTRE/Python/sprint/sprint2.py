import os

juego = {}
juego_mas_descargado = ""
descargas_mas_altas = 0

abrir_archivo = open("juegos.txt", "r")
for linea in abrir_archivo:
    nombre, descargas = linea.strip().split(", ")
    descargas = int(descargas)
    juego[nombre] = descargas
    if descargas > descargas_mas_altas:
        descargas_mas_altas = descargas
        juego_mas_descargado = nombre

if juego_mas_descargado:
    print(f"El juego más descargado es '{juego_mas_descargado}' con {descargas_mas_altas} descargas.")
else:
    print("No se encontraron juegos en el archivo.")
