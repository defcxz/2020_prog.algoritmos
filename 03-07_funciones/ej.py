# Realizar un menu de opciones
# 1.- Llenar arreglo con numeros enteros
# 2.- mostrar arreglo
# 3.- Mostrar todos los elementos pares del arreglo llenado
# 4.- Mostrar todos los elementos en posicion impar del arreglo
# 5.- Dejar en un segundo arreglo todos los elementos que sean divisibles por 5, 
# mostrar ese arreglo
# 6.- Salir del menu
# ojo, las opciones 2,3,4 y 5 se haran solo si ya se lleno el arreglo
import os

def llenar(arreglo, n):
    sw=True
    while(sw==True):
        try:
            n=int(input("Cuantos numeros desea ingresar? "))
            if(n>0):
                sw=False
            else:
                print("Debe ingresar una cantidad positiva")
        except ValueError:
                print("Debe ingresar un numero entero")
        
    for i in range(n):
        sw=True
        while(sw==True):
            try:
                num=int(input("Ingrese un numero  "))
                sw=False
            except ValueError:
                print("Debe ingresar un numero entero")
        arreglo.append(num)


def mostrar(arreglo, sw1):
    if(sw1==1):
        print(arreglo) #muestro el arreglo
    else:
        print("Debe llenar el arreglo antes de mostrarlo ")

arreglo = []