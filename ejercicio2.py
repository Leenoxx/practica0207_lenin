# Escribir una función que pida un número entero entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de
# ese número, donde n es el número introducido, y la muestre
# por pantalla. Si el fichero no existe debe mostrar
# un mensaje por pantalla informando de ello.
import os


def comprobar_fichero(num_entero):
    if num_entero in range(1, 11):
        if os.path.isfile("tabla-" + str(num_entero) + ".txt"):
            file = open("tabla-" + str(num_entero) + ".txt", "r")
            print(file.read())
            file.close()
        else:
            print("Fichero no creado")
    else:
        print("Número de fichero incorrecto")


num = int(input("Introduce un número entre 1 y 10: "))
comprobar_fichero(num)
