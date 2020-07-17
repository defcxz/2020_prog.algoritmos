x = 0
edad_mayor = 0
edad_menor = 0
suma_edades = 0
sexo_mayor = ''

while(x < 2):
    x += 1
    nom = input('Ingrese el nombre de la persona:\n')
    edad = int(input('Ahora, ingrese la edad:\n'))
    sexo = input('Ahora, ingrese el sexo. Masculino (M) o Femenino (F)\n')
    est_civil = input('Por último, ingrese el estado civil:\n')
    
    suma_edades += edad

    if(edad > edad_menor):
        edad_menor = edad
        civil_menor = est_civil
    if(edad > edad_mayor):
        sexo_mayor = sexo
        civil_mayor = est_civil

print('El sexo de la persona mayor es',sexo_mayor,'y su estado civil es',civil_mayor)
print('La edad de la persona menor es',edad_menor,'y su estado civil es',civil_menor)
print('El promedio de las edades ingresadas es',suma_edades//x)