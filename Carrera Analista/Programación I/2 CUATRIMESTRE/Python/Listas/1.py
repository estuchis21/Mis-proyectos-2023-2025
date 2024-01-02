#  Ingresar 5 elementos para una lista e imprimir el promedio de sus elementos
numeros = []
for i in range (5):
    ingrese_numeros = int(input("Ingrese números para la lista: "))
    numeros.append(ingrese_numeros)
    promedio= sum(numeros) /len(numeros)
    
    print ("El promedio es", promedio)
    