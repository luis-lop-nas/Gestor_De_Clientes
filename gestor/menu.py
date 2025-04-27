# gestor/menu.py

import gestor.helpers as helpers
import gestor.database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print("  GESTOR DE CLIENTES    ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        opcion = input("> ").strip()

        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando clientes...\n")
            if not db.Clientes.lista:
                print("No hay clientes registrados.")
            else:
                for cliente in db.Clientes.lista:
                    print(cliente)
        elif opcion == '2':
            print("Buscando cliente...\n")
            dni = helpers.leer_texto(3, 3, "Introduce el DNI (2 números y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo cliente...\n")
            while True:
                dni = helpers.leer_texto(3, 3, "Introduce el DNI (2 números y 1 letra)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Introduce el nombre (entre 2 y 30 caracteres)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Introduce el apellido (entre 2 y 30 caracteres)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '4':
            print("Modificando cliente...\n")
            dni = helpers.leer_texto(3, 3, "Introduce el DNI del cliente a modificar (2 números y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Introduce el nuevo nombre [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Introduce el nuevo apellido [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            print("Borrando cliente...\n")
            dni = helpers.leer_texto(3, 3, "Introduce el DNI del cliente a borrar (2 números y 1 letra)").upper()
            cliente = db.Clientes.borrar(dni)
            if cliente:
                print("Cliente borrado correctamente.")
            else:
                print("Cliente no encontrado.")
        elif opcion == '6':
            print("Saliendo...\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

        input("\nPresiona ENTER para continuar...")
