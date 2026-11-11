
import sqlite3

def inicializar_db():
    conexion = None

    try:
        conexion = sqlite3.connect('alumnos_talentotech.db')
        cursor = conexion.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER NOT NULL,
                curso TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        conexion.commit()
        print("Base de datos y tabla 'alumnos' creadas exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    except sqlite3.IntegrityError as e:
        print(f"Ya existe la base de datos: {e}")

    finally:
        if conexion:
            conexion.close()
