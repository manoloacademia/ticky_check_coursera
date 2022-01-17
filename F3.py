#usr/bin/#!/usr/bin/env python3
#se define una funcion que encripta con F+3
def cifrar_F3(mensaje):
    salida = []
    for i in mensaje:
        salida.append(str(int(i)+3))
    return salida
