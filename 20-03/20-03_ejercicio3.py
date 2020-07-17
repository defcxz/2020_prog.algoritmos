ano = int(input("Ingrese el año actual:\n"))
ano2 = int(input("Ingrese otro año:\n"))

res = ano - ano2

if(res > 0):
    print("Han pasado",res,"años desde ",ano,"hasta ",ano2)
elif(res < 0):
    res = res-res-res
    print("Faltan",res,"años para llegar a ese año")
else:
    print("Es el mismo año")