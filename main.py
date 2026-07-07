# main.py

from museo_db import crear_tabla
from museo_app import *
from auth import login
from config import BIENVENIDA

def menu():
    """
    Muestra el menú principal del sistema.
    """
    while True:
        print(f"\n{BIENVENIDA}")
        print("1. Registrar obra")
        print("2. Ver obras")
        print("3. Buscar obra")
        print("4. Actualizar obra")
        print("5. Eliminar obra")
        print("6. Reporte")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_obra()
        elif opcion == "2":
            mostrar_obras()
        elif opcion == "3":
            buscar_obra()
        elif opcion == "4":
            actualizar_obra()
        elif opcion == "5":
            eliminar_obra()
        elif opcion == "6":
            reporte_obras()
        elif opcion == "7":
            print("👋 Saliendo del sistema")
            break
        else:
            print("❌ Opción inválida")


# Punto de inicio del programa
if __name__ == "__main__":
    crear_tabla()   # crea la base si no existe

    if login():     # verifica acceso
        menu()      # muestra el sistema