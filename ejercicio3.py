# Escribir una función que pida dos números n y m entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de
# ese número, y muestre por pantalla la línea m del fichero.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os


def comprobar_fichero(num_lista, linea_lista):
    if num_lista in range(1, 11):
        if linea_lista in range(1, 11):
            if os.path.isfile("tabla-" + str(num_lista) + ".txt"):
                file = open("tabla-" + str(num_lista) + ".txt", "r")
                print(file.readlines()[linea_lista - 1])
                file.close()
            else:
                print("Fichero no creado")
        else:
            print("El segundo número no esta entre 1 y 10")
    else:
        print("Número de fichero incorrecto")


n = int(input("Introduce un número entre 1 y 10: "))
m = int(input("Introduce un número entre 1 y 10: "))

comprobar_fichero(n, m)
