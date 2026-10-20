"""
Ejemplo:
un profesor necesira crear un programa que le ayude a calcular el
promedio de notas de un salon de clases.
El ingresa el nombre y el valor de la nota final de cada estudiante.
Al final necesita saber cual es el mejor estudiante y el promedio de
todo el curso.
cada nota es de 0 a 5.0.
"""

cantidad_estudiantes = int(input("cantidad de estudiantes?"))

mejor_estudiante = ""
Nota_mayor = 0.0
suma = 0.0
promedio = 0.0

for veces in range(1, cantidad_estudiantes+1):
    print("estudiante #", veces)
    nombre = input("nombre? ")
    nota = float(input("nota? "))

    suma = suma + nota # <--- Acomuladores

       if nota > nota_mayor: #Encontar el estudiante con mayor nota
        nota_mayor = nota
        mejor_est = nombre

promedio = suma / cantidad_est

print("El promedio del curso es:", promedio)
print("El mejor estudiante es: ", mejor_est, " con nota de:", nota_mayor)
