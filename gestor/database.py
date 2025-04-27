# gestor/database.py

import csv
import gestor.config as config

class Cliente:
    """
    Representa un cliente con DNI, nombre y apellido.
    """

    def __init__(self, dni: str, nombre: str, apellido: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f"({self.dni}) {self.nombre} {self.apellido}"


class Clientes:
    """
    Gestiona la lista de clientes y operaciones sobre ellos.
    """

    lista = []

    # Cargar clientes desde el archivo CSV
    try:
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            for dni, nombre, apellido in reader:
                cliente = Cliente(dni, nombre, apellido)
                lista.append(cliente)
    except FileNotFoundError:
        print(f"Archivo {config.DATABASE_PATH} no encontrado. No se cargaron clientes.")
    except Exception as e:
        print(f"Error al cargar clientes: {e}")

    @staticmethod
    def guardar():
        """
        Guarda la lista de clientes actual en el archivo CSV.
        """
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))

    @staticmethod
    def buscar(dni: str):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None

    @staticmethod
    def crear(dni: str, nombre: str, apellido: str):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni: str, nombre: str, apellido: str):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                cliente.nombre = nombre
                cliente.apellido = apellido
                Clientes.guardar()
                return cliente
        return None

    @staticmethod
    def borrar(dni: str):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente_borrado = Clientes.lista.pop(i)
                Clientes.guardar()
                return cliente_borrado
        return None