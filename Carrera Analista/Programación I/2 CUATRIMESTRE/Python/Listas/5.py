#  Ingresar dos listas de cinco números enteros y luego armar una tercer lista con los productos de cada elemento

lista1 = []
lista2 = []
lista3 = []

for i in range(5):
    num = int(input("Ingrese un numero: "))
    lista1.append(num)
    num2 = int(input("Ingrese un numero: "))
    lista2.append(num2)

    productos = lista1[i] * lista2[i]
    lista3.append(productos)

print(lista3)