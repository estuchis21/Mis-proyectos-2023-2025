lista1 = []
lista2 = []

for i in range(6):
    num = int(input("Ingrese un número para la primera lista: "))
    lista1.append(num)
    
for i in range(6):
    num2 = int(input("Ingrese un número para la segunda lista: "))
    lista2.append(num2)

condicion_cumplida = "Sí"  # Suponemos inicialmente que la condición se cumple

for i in range(6):
    if lista1[i] != lista2[i] * 2:
        condicion_cumplida = "No"
        break

if condicion_cumplida == "Sí":
    print("Los números de la segunda lista son el doble de los de la primera.")
else:
    print("No cumple con la condición.")

