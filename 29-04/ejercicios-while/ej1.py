i = 0
suma = 0
conta = 0
ceros_ingresados = 0
total = 0

while(i < 100):
    i += 1
    ingreso = int(input("Ingrese un número: "))
    if(ingreso > 3):
        total += ingreso
    if(ingreso > 0):
        suma += ingreso
        conta += 1
    if(ingreso == 0):
        ceros_ingresados += 1
prom = suma/conta


print()
print("La suma total de los números mayores a 3 es",total)
print("El promedio de los números positivos ingresados es de",prom)
print("Se ha ingresado un total de",ceros_ingresados,"ceros.")