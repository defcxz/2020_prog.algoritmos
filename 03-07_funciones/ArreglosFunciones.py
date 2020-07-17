import os #para limpiar pantalla
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
        print(arreglo)
    else:
        print("Debe llenar el arreglo antes de mostrarlo ")
    
def elepares(arreglo, sw1):
    if(sw1==1):
        for i in range(len(arreglo)):
            if(arreglo[i] % 2 == 0):
                print(arreglo[i]) #muestro el arreglo
    else:
        print("Debe llenar el arreglo antes de mostrarlo ")

def posimpar(arreglo, sw1):
    if(sw1==1):
        for i in range(len(arreglo)):
            if(not arreglo.index(i) % 2 == 0):
                print(arreglo[i]) #muestro el arreglo
    else:
        print("Debe llenar el arreglo antes de mostrarlo ")

def segundo(arreglo, sw1):
    if(sw1==1):
        for i in range(len(arreglo)):
            if(arreglo[i] % 5 == 0):
                secarreglo.append(arreglo[i]) #muestro el arreglo
        print("El segundo arreglo quedaría tal que así:",secarreglo)
    else:
        print("Debe llenar el arreglo antes de mostrarlo ")
    
#programa principal		
seguir=True 
arreglo=[] 
secarreglo=[]
sw1=0
while(seguir):
    os.system('cls')
    print("---- MENU PRINCIPAL ----")
    print("1. Llenar arreglo")
    print("2. Mostrar Arreglo")
    print("3. Mostrar todos los elementos pares del arreglo llenado")
    print("4. Mostrar todos los elementos en posicion impar del arreglo")
    print("5. Dejar en un segundo arreglo todos los elementos que sean divisibles por 5, mostrar ese arreglo")
    print("6. Salir del menu")
    correcto=False
    n=0
    while(not correcto):
        try:
            op=int(input("Digite opción 1,2,3,4,5 o 6: "))
            if(op>0 and op<7):
                correcto=True
        except ValueError:
            print('Error, debe ingresar 1,2,3,4,5 o 6')
    
    if(op == 1):
        sw1=1 #cambio el sw1 a uno
        llenar(arreglo, n)         #llamada a función - def.
    elif(op == 2):
        mostrar(arreglo,sw1) 
        pausa=input("Presione enter para continuar")
    elif(op == 3):
        elepares(arreglo, sw1)
        pausa=input("Presione enter para continuar")
    elif(op == 4):
        posimpar(arreglo,sw1)
        pausa = input("Presione enter para continuar")
    elif(op == 5):
        segundo(arreglo,sw1)
        pausa = input("Presione enter para continuar")
    if(op==6):
        print("Gracias, nos vemos pronto!")     
        seguir=False 