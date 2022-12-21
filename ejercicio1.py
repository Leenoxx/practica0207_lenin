# Escribir una función que pida un número entero entre 1 y 10
# y guarde en un fichero con el nombre tabla-n.txt la tabla
# de multiplicar de ese número, donde n es el número introducido.

def tabla_multiplicar(num_entero):
    if num_entero in range(1, 11):
        file = open("tabla-" + str(num_entero) + ".txt", "w")
        for num in range(1, 11):
            file.write(str(num_entero) + " * " + str(num) + " = " + str(num*num_entero) + "\n")
        file.close()
    return


numero = int(input("Introduce un número entre 1 y 10: "))
tabla_multiplicar(numero)
