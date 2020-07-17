n1 = int(input("Ingrese un número:\n"))
n2 = int(input("Ingrese otro número:\n"))
n3 = int(input("Ingrese un último número:\n"))

if(n1==n2):
    print(n1,"es igual a",n2)
elif(n1==n3):
    print(n1,"es igual a",n3)
elif (n2==n3):
    print(n2,"es igual a",n3)
else:
    print("Todos son diferentes")