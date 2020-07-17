contaSolt = 0
contaViudos = 0
maxNombre = ""
maxPeso = 0
eds = ""

n1 = input("Ingrese el nombre de la primera persona.\n")
ed1 = int(input("Ingrese la edad de la persona ingresada.\n"))
sx1 = input("Ingrese F o M, dependiendo del sexo de la persona.\n")
estCivil1 = input("Ingrese soltero/casado/viudo/otro, dependiendo del estado civil de la persona.\n")
alt1 = int(input("Ingrese la altura de la persona en centímetros.\n"))
peso1 = int(input("Ahora, ingrese el peso de la persona en kilos.\n"))

if(alt1 > 170 and peso1 < 80):
    eds = str(ed1)
if(estCivil1 == "soltero"):
    contaSolt += 1
if(sx1 == "M" and estCivil1 == "viudo"):
    contaViudos += 1


n2 = input("Ingrese el nombre de la primera persona.\n")
ed2 = int(input("Ingrese la edad de la persona ingresada.\n"))
sx2 = input("Ingrese F o M, dependiendo del sexo de la persona.\n")
estCivil2 = input("Ingrese soltero/casado/viudo/otro, dependiendo del estado civil de la persona.\n")
alt2 = int(input("Ingrese la altura de la persona en centímetros.\n"))
peso2 = int(input("Ahora, ingrese el peso de la persona en kilos.\n"))

if(alt2 > 170 and peso2 < 80):
    eds = eds+str( - ed2)
if(estCivil2 == "soltero"):
    contaSolt += 1
if(sx2 == "M" and estCivil2 == "viudo"):
    contaViudos += 1


n3 = input("Ingrese el nombre de la primera persona.\n")
ed3 = int(input("Ingrese la edad de la persona ingresada.\n"))
sx3 = input("Ingrese F o M, dependiendo del sexo de la persona.\n")
estCivil3 = input("Ingrese soltero/casado/viudo/otro, dependiendo del estado civil de la persona.\n")
alt3 = int(input("Ingrese la altura de la persona en centímetros.\n"))
peso3 = int(input("Ahora, ingrese el peso de la persona en kilos.\n"))

if(alt3 > 170 and peso3 < 80):
    eds = eds+str( - ed3)
if(estCivil3 == "soltero"):
    contaSolt += 1
if(sx3 == "M" and estCivil3 == "viudo"):
    contaViudos += 1


n4 = input("Ingrese el nombre de la primera persona.\n")
ed4 = int(input("Ingrese la edad de la persona ingresada.\n"))
sx4 = input("Ingrese F o M, dependiendo del sexo de la persona.\n")
estCivil4 = input("Ingrese soltero/casado/viudo/otro, dependiendo del estado civil de la persona.\n")
alt4 = int(input("Ingrese la altura de la persona en centímetros.\n"))
peso4 = int(input("Ahora, ingrese el peso de la persona en kilos.\n"))

if(alt4 > 170 and peso4 < 80):
    eds = eds+str( - ed4)
if(estCivil4 == "soltero"):
    contaSolt += 1
if(sx4 == "M" and estCivil4 == "viudo"):
    contaViudos += 1


n5 = input("Ingrese el nombre de la primera persona.\n")
ed5 = int(input("Ingrese la edad de la persona ingresada.\n"))
sx5 = input("Ingrese F o M, dependiendo del sexo de la persona.\n")
estCivil5 = input("Ingrese soltero/casado/viudo/otro, dependiendo del estado civil de la persona.\n")
alt5 = int(input("Ingrese la altura de la persona en centímetros.\n"))
peso5 = int(input("Ahora, ingrese el peso de la persona en kilos.\n"))

if(alt5 > 170 and peso5 < 80):
    eds = eds+str( - ed5)
if(estCivil5 == "soltero"):
    contaSolt += 1
if(sx5 == "M" and estCivil5 == "viudo"):
    contaViudos += 1

if(peso1 > peso2 and peso1 > peso3 and peso1 > peso4 and peso1 > peso5):
    maxNombre = n1
    maxPeso = peso1
elif(peso2 > peso1 and peso2 > peso3 and peso2 > peso4 and peso2 > peso5):
    maxNombre = n2
    maxPeso = peso2
elif(peso3 > peso1 and peso3 > peso2 and peso3 > peso4 and peso3 > peso5):
    maxNombre = n3
    maxPeso = peso3
elif(peso4 > peso1 and peso4 > peso2 and peso4 > peso3 and peso4 > peso5)):
    maxNombre = n4
    maxPeso = peso4
else:
    maxNombre = n5
    maxPeso = peso5

print("El total de personas solteras es de",contaSolt)
print("Hay un total de",contaViudos,"hombres viudos.")
print("La persona con mayor peso es",maxNombre,"con un peso de",maxPeso,"kilos")
print("La edad de las personas que miden más de 1.70 y pesan menos de 80 kilos son:",eds)