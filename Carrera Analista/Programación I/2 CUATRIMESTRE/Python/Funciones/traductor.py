# Solicitar al usuario el ingreso de una oración por teclado. Puede ser una palabra o mas.

def traducir(palabra):
    lista_palabras_español = ["Hola", "mundo"]
    lista_palabras_ingles = ["Hello", "world"]
    t = palabra
    if palabra in lista_palabras_español: 
        indice_español = lista_palabras_español.index(palabra)
        t = lista_palabras_ingles[indice_español]
    return t

# inicio del programa
traduccion = ""

for i in input("Ingrese oracion: ").split():
    traduccion += traducir(i) + " "

print(traduccion)






