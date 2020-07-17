# Realizar un programa que me permita el siguiente menu
# 1.- Sumar 2 numeros
# 2.- Restar 2 numeros
# 3.- Salir del menu 
# Dependiendo de la opcion que elija debera llamar a una funcion que lo realice
import os

def suma(n1,n2):
    total = n1+n2
    print('El total de la suma es',total)

def resta(n1,n2):
    total = n1-n2
    print('El total de la resta es',total)

x = False
while (x == False):
    try:
        os.system('cls')
        ing = int(input('INGRESE UNA OPCIÓN:\n1 - Sumar dos números\n2 - Restar dos números\n3 - SALIR\n'))
        if(ing == 1 or ing == 2 or ing == 3):
            x = True
        else:
            print('Ingrese una de las opciones mostradas anteriormente.')
    except:
        print('Ingrese una opción válida.')

if(ing == 1):
    valida = False
    while(valida == False):
        os.system('cls')
        try:
            n1 = int(input('Ingrese un número.\n'))
            valida = True
        except:
            print('Ingrese un número válido.')
    valida = False
    while(valida == False):
        try:
            n2 = int(input('Ingrese otro número.\n'))
            valida = True
        except:
            print('Ingrese un número válido.')
    suma(n1,n2)
elif(ing == 2):
    os.system('cls')
    valida = False
    while(valida == False):
        try:
            n1 = int(input('Ingrese un número.\n'))
            valida = True
        except:
            print('Ingrese un número válido.')
    valida = False
    while(valida == False):
        try:
            n2 = int(input('Ingrese otro número.\n'))
            valida = True
        except:
            print('Ingrese un número válido.')
    resta(n1,n2)
else:
    print('Adiós.')