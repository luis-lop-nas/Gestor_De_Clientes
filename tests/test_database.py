

# tests/test_database.py

import unittest
import gestor.database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba: reseteamos los clientes
        db.Clientes.lista = [
            db.Cliente("15J", "Marta", "Pérez"),
            db.Cliente("48H", "Manolo", "López"),
            db.Cliente("28Z", "Ana", "García")
        ]

    def test_buscar_cliente_existente(self):
        cliente = db.Clientes.buscar("15J")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nombre, "Marta")

    def test_buscar_cliente_inexistente(self):
        cliente = db.Clientes.buscar("99X")
        self.assertIsNone(cliente)

    def test_crear_cliente(self):
        nuevo = db.Clientes.crear("77Y", "Lucía", "Sánchez")
        self.assertEqual(nuevo.dni, "77Y")
        self.assertEqual(len(db.Clientes.lista), 4)

    def test_modificar_cliente(self):
        modificado = db.Clientes.modificar("48H", "Manu", "López")
        self.assertEqual(modificado.nombre, "Manu")

    def test_borrar_cliente(self):
        borrado = db.Clientes.borrar("28Z")
        self.assertEqual(borrado.dni, "28Z")
        self.assertEqual(len(db.Clientes.lista), 2)

if __name__ == "__main__":
    unittest.main()