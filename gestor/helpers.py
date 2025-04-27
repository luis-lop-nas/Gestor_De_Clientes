# gestor/helpers.py

import os
import platform
import re

def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal según el sistema operativo.
    """
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    """
    Lee un texto del usuario con restricciones de longitud.
    """
    if mensaje:
        print(mensaje)
    while True:
        texto = input("> ").strip()
        if longitud_min <= len(texto) <= longitud_max:
            return texto
        print(f"Debe tener entre {longitud_min} y {longitud_max} caracteres.")


def dni_valido(dni, lista_clientes):
    """
    Valida que el DNI tenga formato correcto (2 números y 1 letra mayúscula) y que no esté repetido.
    """
    if not re.match(r'^[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe tener 2 números y 1 letra mayúscula.")
        return False
    for cliente in lista_clientes:
        if cliente.dni == dni:
            print("DNI ya registrado en otro cliente.")
            return False
    return True
