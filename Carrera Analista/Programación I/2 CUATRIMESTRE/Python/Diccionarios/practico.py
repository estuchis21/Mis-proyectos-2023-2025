# Definición de funciones

# Ingresar jugadores al plantel
def ingresar_jugador(plantel):
    numero_camiseta = input("Ingrese el número de camiseta del jugador: ")
    apellido_jugador = input("Ingrese el apellido del jugador: ")
    # Agregamos la información al diccionario "plantel" usando el número de camiseta como clave
    plantel[numero_camiseta] = apellido_jugador

# Equipo inicial
def ingresar_equipo_inicial(plantel):
    equipo = {}  # Creamos un nuevo diccionario llamado "equipo" para el equipo inicial
    print("Ingrese los números de los 11 jugadores para el equipo inicial:")
    for i in range(11):
        numero_camiseta = input(f"Jugador {i+1}: ")
        # Verificamos si el número de camiseta existe en el diccionario "plantel"
        if numero_camiseta in plantel:
            # Si existe, agregamos al jugador al equipo inicial
            equipo[numero_camiseta] = plantel[numero_camiseta]
            # Eliminamos al jugador del plantel para indicar que está en el equipo inicial
            del plantel[numero_camiseta]
        else:
            print(f"El número de camiseta {numero_camiseta} no está registrado en el plantel.")
    return equipo

# Paso 3
def realizar_cambio(equipo, plantel):
    numero_salida = input("Ingrese el número de camiseta del jugador que va a salir: ")
    numero_ingreso = input("Ingrese el número de camiseta del jugador que va a ingresar: ")
    # Verificamos si los números de camiseta existen en el diccionario "equipo"
    if numero_salida in equipo and numero_ingreso in plantel:
        # Sacamos al jugador que sale del equipo
        jugador_salida = equipo.pop(numero_salida)
        # Agregamos al jugador que ingresa al equipo
        equipo[numero_ingreso] = plantel[numero_ingreso]
        # Movemos al jugador que sale al plantel
        plantel[numero_salida] = jugador_salida
    else:
        print("Uno o ambos números de camiseta no son válidos.")

# Paso final
def mostrar_formacion(equipo):
    print("Formación del equipo al final del partido:")
    for numero_camiseta, apellido_jugador in equipo.items():
        print(f"Número de camiseta: {numero_camiseta}, Apellido: {apellido_jugador}")

# Paso uno
def main():
    # Creamos un diccionario llamado "plantel" para almacenar la información de los jugadores
    plantel = {}
    # Solicitamos al operador cuántos jugadores quiere ingresar
    num_jugadores = int(input("Ingrese la cantidad de jugadores que desea registrar en el plantel: "))   
    # Pedimos al operador que ingrese la información de cada jugador
    for i in range(num_jugadores):
        print(f"Ingresando datos del jugador {i+1}:")
        ingresar_jugador(plantel)
    equipo_inicial = ingresar_equipo_inicial(plantel)
    # Bucle para realizar cambios o finalizar el partido
    while True:
        print("\nOpciones:")
        print("1. Realizar un cambio en el equipo.")
        print("2. Finalizar el partido.")
        opcion = input("Seleccione una opción (1/2): ")        
        if opcion == "1":
            realizar_cambio(equipo_inicial, plantel)
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")
    mostrar_formacion(equipo_inicial)
if __name__ == "__main__":
    main()
    
