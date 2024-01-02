# Pedir al usuario que ingrese una lista de seis números enteros
lista_original = []
for i in range(6):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    lista_original.append(numero)

# Crear una nueva lista con los elementos duplicados
lista_duplicada = [x * 2 for x in lista_original]

# Mostrar la lista duplicada
print("Lista Original:", lista_original)
print("Lista Duplicada:", lista_duplicada)
