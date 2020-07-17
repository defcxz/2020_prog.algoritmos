opc = input("Bienvenido! Le gustaría una pizza vegetariana? Ingrese S o N: ")

if(opc == "S"):
    print("========= Ha elegido la pizza vegetariana =========")
    print("Los ingredientes disponibles son:\n1 - Pimiento\n2 - Tofu\nSin contar la mozzarella y el tomate")
    ingrediente = input("Ingrese el ingrediente deseado.")

    print("========= RESUMEN =========\nUsted eligió la pizza vegetariana, y los ingredientes que llevará son:\n- Mozzarella\n- Tomate\n-",ingrediente)
elif(opc == "N"):
    print("========= Ha elegido la pizza no vegetariana. =========")
    print("Los ingredientes disponibles son:\n1 - Pepperoni\n2 - Jamón\n3 - Salmón\nSin contar la mozzarella y el tomate")
    ingrediente = input("Ingrese el ingrediente deseado.")

    print("========= RESUMEN =========\nUsted eligió la pizza NO vegetariana, y los ingredientes que llevará son:\n- Mozzarella\n- Tomate\n-",ingrediente)
else:
    print("Ha ocurrido un error. Por favor, inténtelo nuevamente")