# EJ1_Mostrar porcentaje de hombres y mujeres en un salón de clases, ingresando el total de hombres y mujeres

muj = int(input("Ingrese el número total de mujeres:\n"))
hom = int(input("Ahora, ingrese el número total de hombres:\n"))

total = muj+hom

porcMuj =total * (muj/100)
porcHom =total * (hom/100)

print("El total de personas en el salón de clases es de",total,",en el que las mujeres son el ",porcMuj,"% y los hombres son el ",porcHom,"%.")

#EJ2_Dada una cantidad de artículos y su precio bruto, calcular y mostrar total invertido, precio de venta, total venta

#EJ3_Cálculo de area de un triángulo

ingBase = int(input("Ingrese la base del triángulo:\n"))
ingAlt = int(input("Ingrese la altura del triángulo:\n"))

area = (ingBase*ingAlt)/2

print("El área del triángulo es de:",area)