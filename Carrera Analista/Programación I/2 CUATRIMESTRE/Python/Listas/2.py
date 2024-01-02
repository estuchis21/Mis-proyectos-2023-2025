lista_string = []
cantidad_a_ingresar = int(input("Ingrese la cantidad de palabras para la lista: "))

for i in range(cantidad_a_ingresar):
    palabra = input(f"Ingrese la palabra número {i + 1}: ")
    lista_string.append(palabra)

lista_string.reverse()

print("Lista invertida:")
for palabra in lista_string:
    print(palabra)



