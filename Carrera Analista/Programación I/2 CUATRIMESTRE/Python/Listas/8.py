lista = []

for i in range(10):
    nums = int(input(f"Ingrese el número: {i + 1}: "))
    lista.append(nums)
    #indice
indice_max = lista.index(max(lista))
    #mostrar el mayor
print("El mayor es: ", max(lista), "en el índice: ", indice_max)




