i = 0
contapares = 0
mult = 1
impares = ""

while(i < 100):
    i += 1
    ing = int(input('Ingrese un número: '))
    if(ing % 2 == 0):
        contapares += 1
    else:
        impares += " "+str(ing)
    if(ing < 0):
        mult *= ing

print()
print('Se han ingresado',contapares,'números pares')
print('Los números impares son',impares)
if(mult != 1):
    print('El total de la multiplicación de los negativos es',mult)
else: 
    print('No se ha ingresado ningún número negativo lel')