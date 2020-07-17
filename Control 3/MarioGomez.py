import os

def ingresar(nombre_vendedor, n):
    valida = False
    while(valida == False):
        try:
            n = int(input('Ingrese la cantidad de vendedores que desea ingresar.\n'))
            if(n > 0):
                valida = True
            else:
                print('Ingrese, por favor, un número mayor a cero.')
        except:
            print('Ingrese un valor válido. Inténtelo nuevamente.')

    for i in range(n):
        nombre = ''
        while(len(nombre) <= 5):
            nombre = input('Ingrese el nombre del vendedor: ')
            if(len(nombre) > 5):
                nombre_vendedor.append(nombre)
                print('Se ha ingresado',nombre,'al arreglo.')
                i += 1
            else:
                print('Debe ingresar un nombre con más de 5 caracteres.')
                nombre = ''



nombre_vendedor = []
numero_vendedor = []
cantidad_globos = []
color_globo = []
n = 0
os.system('cls')
sw = True
while(sw == True):
    try:
        print('*'*20,'Redondito.com','*'*20,'\n1. Ingresar\n2. Mostrar\n3. Total de dinero recaudado por todos los vendedores\n4. Salir')
        correcto = False
        while(not correcto):
            try:
                opcion=int(input("Digite opción 1,2,3 o 4: "))
                if(opcion >= 1 and opcion <= 4):
                    correcto=True
            except ValueError:
                print('Error, debe ingresar una opción válida')
    except:
        os.system('cls')
        print('\n = Ingrese un valor válido. =\n')

    if(opcion == 1):
        ingresar(nombre_vendedor, n)
        
    elif(opcion == 4):
        sw = False