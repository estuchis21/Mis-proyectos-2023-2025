dni=[38333444,28555666,22333444,38333444]
materia=['Algebra','Algebra','Ingles','Programación I']
nota=[8,2,5,9]

# A continuación se debe generar un algoritmo que le solicite al usuario que ingrese por consola un número de dni, y luego se debe listar en la misma consola  todas las materias con su nota, siempre y cuando haya sido aprobada. La nota para la aprobación es mayor o igual a 4.
ingreso_dni = int(input("Ingrese su DNI: "))
if ingreso_dni in dni:
    print ("Usted acaba de rendir: ", materia[dni.index(ingreso_dni)])
else:
    print ("No se encuentra el DNI")
suma_notas = 0
materias_aprobadas = 0
for i in range(len(dni)):
    if dni[i] == ingreso_dni and nota[i] >= 4:
        print (f"La nota del alumno {ingreso_dni} es {nota[i]} en la asignatura: {materia[i]}. Y está aprobado.")

        suma_notas += nota[i]
        materias_aprobadas += 1

# sacar promedio
promedio = suma_notas / materias_aprobadas
print (f"El promedio obtenido por el alumno con DNI {ingreso_dni} es: {promedio}")

    


