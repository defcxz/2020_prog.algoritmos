#Ingrese nombre y edad de dos personas, mostrar:
#    El nombre de la persona mayor
#    La edad de la persona menor
#    Nombre y edad de ambos si sus edades son iguales

nom1 = input("Ingrese el nombre de una persona:\n")
ed1 = int(input("Ingrese la edad de esa persona:\n"))

nom2 = input("Ingrese el nombre de otra persona:\n")
ed2 = int(input("Ingrese la edad de esta otra persona:\n"))

if(ed1 > ed2):
    print(nom1,"es la persona mayor")
    print("La persona menor tiene",ed2,"años")
if(ed2 > ed1):
    print(nom2,"es la persona mayor")
    print("La persona menor tiene",ed1,"años")
else:
    print("Las edades son iguales entre",nom1,"con",ed1,"años, y",nom2,"con",ed2,"años.")