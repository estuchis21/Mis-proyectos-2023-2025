def IngresarLista():
    n = int(input("Ingrese la cantidad de elementos en la lista: "))
    lista = []
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i+1}: "))
        lista.append(elemento)
    return lista

def MostrarSuma(lista):
    suma = sum(lista)
    print("La suma de todos los elementos es:", suma)

def MostrarPromedio(lista):
    promedio = sum(lista) / len(lista)
    print("El promedio de los elementos es:", promedio)

def MostrarMayor(lista):
    mayor = max(lista)
    print("El elemento mayor es:", mayor)

def MostrarMenor(lista):
    menor = min(lista)
    print("El elemento menor es:", menor)

def CambiarSigno(lista):
    signo_cambiado = [-x for x in lista]
    return signo_cambiado

def InvertirOrden(lista):
    orden_invertido = lista[::-1]
    return orden_invertido

# Llamadas a las funciones
lista_ingresada = IngresarLista()
MostrarSuma(lista_ingresada)
MostrarPromedio(lista_ingresada)
MostrarMayor(lista_ingresada)
MostrarMenor(lista_ingresada)

lista_cambiada_signo = CambiarSigno(lista_ingresada)
print("Lista con signos cambiados:", lista_cambiada_signo)

lista_invertida = InvertirOrden(lista_ingresada)
print("Lista con orden invertido:", lista_invertida)