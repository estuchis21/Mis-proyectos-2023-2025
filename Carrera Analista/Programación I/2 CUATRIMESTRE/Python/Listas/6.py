lista1 = []
lista2 = []
iguales = True

for i in range(3):
    numero_lista_1 = int(input("Ingrese un número para la lista 1: "))
    lista1.append(numero_lista_1)
    numero_lista_2 = int(input("Ingrese un número para la lista 2: "))
    lista2.append(numero_lista_2)

    if lista1[i] != lista2[i]:
        iguales = False

if iguales:
    print("Todos los números son iguales.")
else:
    print("Al menos un número no es igual.")

