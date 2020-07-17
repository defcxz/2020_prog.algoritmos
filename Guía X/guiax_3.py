x = 0
sueldo_mayor = 0
conta_hombres = 0
conta_mujeres = 0
sueldoH = 0
sueldoM = 0
nom_mayor = ''
while(x < 2):
    x += 1
    nom = input('Ingrese el nombre del trabajador.\n')
    edad = int(input('Ingrese la edad del trabajador.\n'))
    sexo = input('Indique el sexo del trabajador. (Hombre o Mujer)\n')
    sueldo = int(input('Por último, ingrese el sueldo del trabajador.\n'))

    if(sueldo > sueldo_mayor):
        sueldo_mayor = sueldo
        nom_mayor = nom
    if(sexo.capitalize() == 'Hombre'):
        sueldoH += sueldo
        conta_hombres += 1
    else:
        sueldoM += sueldo
        conta_mujeres += 1
print('='*40)
print('El nombre de la persona con mayor sueldo es',sueldo_mayor)
print('El promedio de sueldos de los hombres es',sueldoH//conta_hombres)
print('El promedio de sueldos de las mujeres es',sueldoM//conta_mujeres)
print('Finalmente, el promedio general de sueldos es de',sueldo//x)
print('='*40)