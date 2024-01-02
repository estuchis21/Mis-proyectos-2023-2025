# Crear las listas de números de mes y cantidad de días
lista1 = []
lista2 = []
nombre_de_mes = []

# Llenar las listas con datos
for i in range(12):
    numero_mes = int(input(f"Ingrese el número de mes {i + 1}: "))
    lista1.append(numero_mes)
    dias_de_mes = int(input(f"Ingrese la cantidad de días del mes {i + 1}: "))
    lista2.append(dias_de_mes)

# Solicitar al usuario que ingrese un número de mes
ingreso_mes = int(input("Ingrese un número de mes para conocer la cantidad de días: "))

# Verificar si el número de mes está en la lista y mostrar la cantidad de días
if ingreso_mes in lista1:
    indice = lista1.index(ingreso_mes)
    cantidad_dias = lista2[indice]
    print(f"El mes {ingreso_mes} tiene {cantidad_dias} días.")
else:
    print("Número de mes no encontrado en la lista.")





