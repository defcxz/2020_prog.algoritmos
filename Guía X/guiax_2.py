x =  0
no_votan = ''

while(x < 30):
    x += 1

    nom = input('Ingrese el nombre de la persona.\n')
    edad = int(input('Ahora, ingrese la edad de esa persona.\n'))
    if(edad < 17):
        no_votan += '-'+nom+'\n'

print('El listado de las peronas que pueden votar son:\n'+no_votan)