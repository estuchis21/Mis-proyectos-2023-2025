def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

while True:
    cantidad_de_entrada = int(input("Ingrese un número para calcular su factorial (0 para salir): "))
    
    if cantidad_de_entrada == 0:
        print("¡Hasta luego!")
        break
    
    if cantidad_de_entrada < 0:
        print("Ingrese un número no negativo.")
    else:
        resultado = calcular_factorial(cantidad_de_entrada)
        print(f"El factorial de {cantidad_de_entrada} es {resultado}")
        
        
calcular_factorial(6)