cantM = 0
cantH = 0
mayorT = 0
menorQ = 0

n1 = input("Ingrese el nombre de la primera persona.\n")
s1 = input("Ingrese F o M, dependiendo del sexo de la primera persona.\n")
ed1 = int(input("Ingrese la edad de la primera persona.\n"))

if(s1 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed1 > 30):
    mayorT += 1
elif(ed1 < 15):
    menorQ += 1
nomMayor = n1
sexMayor = s1
edMayor = ed1

n2 = input("Ingrese el nombre de la segunda persona.\n")
s2 = input("Ingrese F o M, dependiendo del sexo de la segunda persona.\n")
ed2 = int(input("Ingrese la edad de la segunda persona.\n"))

if(s2 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed2 > 30):
    mayorT += 1
elif(ed2 < 15):
    menorQ += 1
if(ed2 > edMayor):
    nomMayor = n2
    sexMayor = s2
    edMayor = ed2

n3 = input("Ingrese el nombre de la tercera persona.\n")
s3 = input("Ingrese F o M, dependiendo del sexo de la tercera persona.\n")
ed3 = int(input("Ingrese la edad de la tercera persona.\n"))

if(s3 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed3 > 30):
    mayorT += 1
elif(ed3 < 15):
    menorQ += 1
if(ed3 > edMayor):
    nomMayor = n3
    sexMayor = s3
    edMayor = ed3


n4 = input("Ingrese el nombre de la cuarta persona.\n")
s4 = input("Ingrese F o M, dependiendo del sexo de la cuarta persona.\n")
ed4 = int(input("Ingrese la edad de la cuarta persona.\n"))

if(s4 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed4 > 30):
    mayorT += 1
elif(ed4 < 15):
    menorQ += 1
if(ed4 > edMayor):
    nomMayor = n4
    sexMayor = s4
    edMayor = ed4


n5 = input("Ingrese el nombre de la quinta persona.\n")
s5 = input("Ingrese F o M, dependiendo del sexo de la quinta persona.\n")
ed5 = int(input("Ingrese la edad de la quinta persona.\n"))

if(s5 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed5 > 30):
    mayorT += 1
elif(ed5 < 15):
    menorQ += 1
if(ed5 > edMayor):
    nomMayor = n5
    sexMayor = s5
    edMayor = ed5


n6 = input("Ingrese el nombre de la sexta persona.\n")
s6 = input("Ingrese F o M, dependiendo del sexo de la sexta persona.\n")
ed6 = int(input("Ingrese la edad de la sexta persona.\n"))

if(s6 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed6 > 30):
    mayorT += 1
elif(ed6 < 15):
    menorQ += 1
if(ed6 > edMayor):
    nomMayor = n6
    sexMayor = s6
    edMayor = ed6


n7 = input("Ingrese el nombre de la séptima persona.\n")
s7 = input("Ingrese F o M, dependiendo del sexo de la séptima persona.\n")
ed7 = int(input("Ingrese la edad de la séptima persona.\n"))

if(s7 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed7 > 30):
    mayorT += 1
elif(ed7 < 15):
    menorQ += 1
if(ed7 > edMayor):
    nomMayor = n7
    sexMayor = s7
    edMayor = ed7


n8 = input("Ingrese el nombre de la octava persona.\n")
s8 = input("Ingrese F o M, dependiendo del sexo de la octava persona.\n")
ed8 = int(input("Ingrese la edad de la octava persona.\n"))

if(s8 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed8 > 30):
    mayorT += 1
elif(ed8 < 15):
    menorQ += 1
if(ed8 > edMayor):
    nomMayor = n8
    sexMayor = s8
    edMayor = ed8

n9 = input("Ingrese el nombre de la novena persona.\n")
s9 = input("Ingrese F o M, dependiendo del sexo de la novena persona.\n")
ed9 = int(input("Ingrese la edad de la novena persona.\n"))

if(s9 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed9 > 30):
    mayorT += 1
elif(ed9 < 15):
    menorQ += 1
if(ed9 > edMayor):
    nomMayor = n9
    sexMayor = s9
    edMayor = ed9


n10 = input("Ingrese el nombre de la décima persona.\n")
s10 = input("Ingrese F o M, dependiendo del sexo de la décima persona.\n")
ed10 = int(input("Ingrese la edad de la décima persona.\n"))

if(s10 == "M"):
    cantH += 1
else:
    cantM += 1
if(ed10 > 30):
    mayorT += 1
elif(ed10 < 15):
    menorQ += 1
if(ed10 > edMayor):
    nomMayor = n10
    sexMayor = s10
    edMayor = ed10

print("La cantidad de mujeres que visitaron el teatro municipal es de",cantM,"\nLa cantidad de hombres que visitaron el teatro es de",cantH)
print("Hubieron",mayorT,"personas mayores que 30 años y",menorQ,"personas menores a 15 años")
print("La persona mayor es",nomMayor,"y su edad es de",edMayor)