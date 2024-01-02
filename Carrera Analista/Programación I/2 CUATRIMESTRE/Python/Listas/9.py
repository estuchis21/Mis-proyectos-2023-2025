lista = []
for i in range(3):
    temperaturas = int(input("Ingrese temperatura: "))
    lista.append(temperaturas)
while True:
        promedio = sum(lista) / len(lista)
        if promedio < 10:
              temperaturas = int(input("Ingrese de vuelta la temperatura: "))
              lista.append(temperaturas)
        else:
              break
        print(lista)
