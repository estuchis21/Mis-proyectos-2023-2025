def contar_apariciones(cadena):
    # Crear un diccionario vacío para almacenar las apariciones
    apariciones = {}
    
    # Iterar a través de cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter ya está en el diccionario, incrementa su contador en 1
        if caracter in apariciones:
            apariciones[caracter] += 1
        # Si el carácter no está en el diccionario, agrégalo con un contador de 1
        else:
            apariciones[caracter] = 1
    
    return apariciones


cadena = input("Ingrese una cadena de texto: ")
resultado = contar_apariciones(cadena)
for caracter, cantidad in resultado.items():
    print(f"'{caracter}': {cantidad}")


