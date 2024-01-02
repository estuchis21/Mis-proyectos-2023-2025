def codigos():
    asignaturas = {}
    cantidad_de_materias = int(input("Ingrese la cantidad de materias a poner en el analítico: "))
    for i in range(cantidad_de_materias):
        asignatura_nombre = input("Ingrese el nombre de la asignatura: ")
        ingreso_codigo_año = int(input(f"Ingrese el código del año para {asignatura_nombre}: "))
        ingreso_codigo_asignatura = int(input(f"Ingrese el código de la asignatura para {asignatura_nombre}: "))
        codigo_completo = str(ingreso_codigo_año) + str(ingreso_codigo_asignatura)
        asignaturas[asignatura_nombre] = codigo_completo
    return asignaturas

def notas(asignaturas):
    analitico = {}
    for asignatura, codigo in asignaturas.items():
        ingreso_notas_asignaturas = int(input(f"Ingrese la nota de la asignatura {asignatura} ({codigo}): "))
        analitico[asignatura] = ingreso_notas_asignaturas
    return analitico

def emitir_analitico(analitico):
    print("Analítico:")
    asignaturas_aprobadas = {asignatura: nota for asignatura, nota in analitico.items() if nota >= 4}
    for asignatura, nota in asignaturas_aprobadas.items():
        print(f"Asignatura: {asignatura}, Nota: {nota}")
    print(f"Cantidad de asignaturas aprobadas: {len(asignaturas_aprobadas)}")

def porcentaje_analítico(asignaturas, analitico):
    cantidad_materias = len(asignaturas)
    asignaturas_aprobadas = len([nota for nota in analitico.values() if nota >= 4])
    porcentaje = (asignaturas_aprobadas / cantidad_materias) * 100
    print(f"Porcentaje de aprobación: {porcentaje}%")

def promedio_analitico(analitico):
    notas_aprobadas = [nota for nota in analitico.values() if nota >= 4]
    if notas_aprobadas:
        promedio = sum(notas_aprobadas) / len(notas_aprobadas)
        print(f"Promedio obtenido: {promedio}")
    else:
        print("No hay asignaturas aprobadas para calcular el promedio.")

def main():
    asignaturas = codigos()
    notas_asignaturas = notas(asignaturas)
    
    while True:
        print("\nMenú de opciones:")
        print("1. Emitir analítico")
        print("2. Porcentaje de aprobación")
        print("3. Promedio obtenido")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4): ")
        
        if opcion == '1':
            emitir_analitico(notas_asignaturas)
        elif opcion == '2':
            porcentaje_analítico(asignaturas, notas_asignaturas)
        elif opcion == '3':
            promedio_analitico(notas_asignaturas)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()