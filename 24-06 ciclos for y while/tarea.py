# Realizar un programa en Python que me llene un arreglo con numeros enteros y positivos.
# Una vez lleno el arreglo
# Mostrar:
# a) El mayor elemento del arreglo
# b) El menor elemento del arreglo
# c) El promedio general de los elementos del arreglo
# d) La suma de todos los numeros positivos del arreglo
# e) Todos los numeros que sean pares.

array = []
num_mayor = 0
num_menor = 0
total = 0
total_positivos = 0
total_par = ''
cant = 0
while (cant == 0):
    try:
        cant = int(input('Cuántos números desea ingresar?\n'))
        if(cant <= 0):
            print('Debe ingresar un número entero y positivo :p')
            cant = 0
    except:
        print('Ingrese un número válido.')
for i in range(cant):
    x = 0
    while (x == 0):
        try:
            x = int(input('Ingrese un número para añadir al arreglo:\n'))
            if(x <= 0):
                print('Debe ingresar un número entero y positivo :p')
                x = 0
        except:
            print('Ingrese un número válido.')
    total += x
    array.append(x)
    if(num_menor == 0):
        if(x > num_menor):
            num_menor = x
    elif(x < num_menor):
        num_menor = x
    elif(x > num_mayor):
        num_mayor = x
    if(x > 0):
        total_positivos += x
    if(x % 2 == 0):
        total_par = ' '+str(x)
       
prom = total//cant

print(array)
print('El número mayor dentro del arreglo es',num_mayor)
print('El número menor, en cambio, es',num_menor)
print('El promedio entre todos los elementos es',prom)
print('La suma de todos los números positivos es',total_positivos)
if(total_par == ''):
    print('No se ha ingresado ningún número par :p')
else:
    print('Los números pares son'+total_par)
