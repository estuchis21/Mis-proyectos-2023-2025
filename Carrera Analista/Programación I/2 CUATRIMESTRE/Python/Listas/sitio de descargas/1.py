software=["OpenOffice","Fortnite","GeoGebra"]
descargas=[1789,650,325]

# primer paso: sumar la cantidad total de descargas

suma_descargas = sum(descargas)

# El juego o aplicación que más descargas a tenido
max_descarga = max(descargas)
nombre_juego_mas_descargado = software[descargas.index(max_descarga)]

print(suma_descargas)
print("El juego mas descargado es: ", nombre_juego_mas_descargado, ". Con ", max_descarga, " descargas.")

#3-Mostrar una lista con las descargas que superaron la cantidad de 500 (mostrar el nombre de softwares del que supere las 500 descargas)

software_500_descargas = []
for i in range(len(software)):
    if descargas[i] >= 500:
        software_500_descargas.append((software[i], descargas[i]))
print("He aquí los juegos con mas de 500 descargas: ", software_500_descargas)






