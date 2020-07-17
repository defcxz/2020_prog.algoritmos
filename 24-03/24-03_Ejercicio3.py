#Ingrese un numero por teclado (del 1 al 7) y muestre con palabras que día de la semana es el numero ingresado

n = int(input("Ingrese un número del 1 al 7\n"))

if (n >= 1 and n <= 7):
    if(n == 1):
        print("El número que usted ha ingresado corresponde al día Lunes")
    elif(n == 2):
        print("El número que usted ha ingresado corresponde al día Martes")
    elif(n == 3):
        print("El número que usted ha ingresado corresponde al día Miércoles")
    elif(n == 4):
        print("El número que usted ha ingresado corresponde al día Jueves")
    elif(n == 5):
        print("El número que usted ha ingresado corresponde al día Viernes")
    elif(n == 6):
        print("El número que usted ha ingresado corresponde al día Sábado")
    elif(n == 7):
        print("El número que usted ha ingresado corresponde al día Domingo")    
else:
    print("Ha ingresado un número inválido. Inténtelo nuevamente.")