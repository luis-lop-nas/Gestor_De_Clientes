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
            # TODO: Implementar listar clientes
        elif opcion == '2':
            print("Buscando cliente...\n")
            # TODO: Implementar buscar cliente
        elif opcion == '3':
            print("Añadiendo cliente...\n")
            # TODO: Implementar añadir cliente
        elif opcion == '4':
            print("Modificando cliente...\n")
            # TODO: Implementar modificar cliente
        elif opcion == '5':
            print("Borrando cliente...\n")
            # TODO: Implementar borrar cliente
        elif opcion == '6':
            print("Saliendo...\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

        input("\nPresiona ENTER para continuar...")
