def calcular_sueldo(horas_trabajadas, valor_hora):
    if horas_trabajadas <= 160:
        sueldo = horas_trabajadas * valor_hora
    else:
        horas_normales = 160
        horas_excedentes = horas_trabajadas - horas_normales
        sueldo = (horas_normales * valor_hora) + (horas_excedentes * valor_hora * 1.5)
    
    return sueldo

# Ingresar la cantidad de empleados
n = int(input("Ingrese la cantidad de empleados: "))
sueldos_calculados = []

# Ingresar datos y calcular sueldos
for i in range(n):
    horas = float(input(f"Ingrese las horas trabajadas para el empleado {i + 1}: "))
    valor_hora = float(input(f"Ingrese el valor por hora para el empleado {i + 1}: "))
    sueldo = calcular_sueldo(horas, valor_hora) # "horas" y "valor_hora" son los que le dan valores numericos a los parametros de la función calcular_sueldo (horas_trabajadas, valor_hora)
    sueldos_calculados.append(sueldo)

# Mostrar sueldos calculados
print("\nSueldos calculados:")
for sueldo in sueldos_calculados:
    print(f"${sueldo}")

