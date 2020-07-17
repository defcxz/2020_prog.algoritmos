i = 0
pos = 0

while(i < 10):
    ing = int(input("Ingrese un número: "))
    i += 1
    # se pregunta si el número ingresado es mayor a 0
    if(ing > 0):
        pos += 1

print('Usted ha ingresado',pos,'números positivos')