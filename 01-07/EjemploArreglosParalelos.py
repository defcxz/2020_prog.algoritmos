# import numpy
nombres=[]
edades=[]
genero=[]
sw=True
while(sw==True):
	try:
		n=int(input("Cuantos datos desea ingresar? "))
		if(n>0):
			sw=False
		else:
			print("El total debe ser positivo")
	except ValueError:
		print("Debe ingresar un total entero")
for i in range(n):
	nom=""
	while(len(nom)<=0):
		nom=input("Ingrese nombre de la persona: ")
		if(len(nom)<=0):
			print("Debe ingresar un dato")
	nombres.append(nom)
	sw=True
	while(sw==True):
		try:
			ed=int(input("Cuantos años tiene la persona? "))
			if(ed>0):
				sw=False
			else:
				print("La edad debe ser positiva")
		except ValueError:
			print("Debe ingresar una edad entera")
	edades.append(ed)
	sex=""
	while(len(sex)<=0):
		sex=input("Ingrese genero de la persona debe ser femenino o Masculino ").lower()
		if(sex!="femenino" and sex!="masculino"):
			print("Debe ingresar Femenino o Masculino")
			sex=""
	genero.append(sex)
for i in range(n):
	print("La persona ", nombres[i], " tiene ", edades[i], " años y su genero es: ",genero[i])

# Mostrar la cantidad de mujeres mayores a 30 años
# El promedio de edades de los hombres
edad_hombres = 0
cant_hombres = 0
cant_mujeres = 0
for i in range(n):
	if(edades[i]>30 and genero[i] == "femenino"):
		cant_mujeres += 1
	elif(genero[i] == "masculino"):
		cant_hombres += 1
		edad_hombres += edades[i]
print("Hay un total de",cant_mujeres,"mujeres mayores a 30 años")
print("El promedio de edad de los hombres son",edad_hombres//cant_hombres)