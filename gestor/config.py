

# gestor/config.py

import sys

# Ruta del archivo CSV que contiene los clientes
DATABASE_PATH = 'clientes.csv'

# Si estamos corriendo tests, cambiar la ruta al CSV de pruebas
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'