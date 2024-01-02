def calcular_factorial(numeros):
    diccionario_factoriales = {}
    while True:
        ingreso_numeros = int(input("Ingrese un número entero (0 para salir): "))
        if ingreso_numeros == 0:
            break
        factorial = 1
        for i in range(1, ingreso_numeros + 1):
            factorial *= i
        
        diccionario_factoriales[ingreso_numeros] = factorial
    
    return diccionario_factoriales

# Llamar a la función y obtener el diccionario de factoriales
diccionario_factoriales = calcular_factorial({})

# Mostrar los números y sus factoriales
for numero, factorial in diccionario_factoriales.items():
    print(f"{numero}: {factorial}")
