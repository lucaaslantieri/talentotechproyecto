import sqlite3, os

from tablas import agregar_alumno, consultar_alumnos, buscar_alumno_por_id, eliminar_alumno_por_id
from connection import inicializar_db

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola al iniciar el programa
        print("=== Gestión de Alumnos ===")
        print("0. Update Table (Solo si es necesario)")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Buscar alumno por ID")
        print("4. Eliminar alumno por ID")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            inicializar_db()
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            consultar_alumnos()
        elif opcion == "3":
            id = input("Ingrese el ID del alumno a buscar: ")
            buscar_alumno_por_id(id)
        elif opcion == "4":
            eliminar_alumno_por_id(input("Ingrese el ID del alumno a eliminar: "))
        elif opcion == "5":
            print("Saliendo del programa...")
            exit()

menu()