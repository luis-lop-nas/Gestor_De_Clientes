

# gestor/database.py

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
        return cliente

    @staticmethod
    def modificar(dni: str, nombre: str, apellido: str):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                cliente.nombre = nombre
                cliente.apellido = apellido
                return cliente
        return None

    @staticmethod
    def borrar(dni: str):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(i)
        return None