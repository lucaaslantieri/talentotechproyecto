import sqlite3

def agregar_alumno(): #funcion de agergar alumno, se conecta a la base de datos y solicita los datos del alumno al usuario, luego los inserta en la tabla alumnos
    conexion = sqlite3.connect("alumnos_talentotech.db")
    cursor = conexion.cursor()

    try: #utilizamos try catch para manejar errores de la base de datos y errores inesperados
        nombre = input("Ingrese el nombre del alumno: ").strip().capitalize()
        apellido = input("Ingrese el apellido del alumno: ").strip().capitalize()
        edad = int(input("Ingrese la edad del alumno: ").strip())
        curso = input("Ingrese el curso del alumno: ").strip().upper()
        email = input("Ingrese el email del alumno: ").strip().lower()

        if(nombre == "" or apellido == "" or curso == "" or email == ""):
            print("Error: Todos los campos son obligatorios y la edad debe ser mayor a 0.")
            return
        if edad < 18 or edad > 100:
            print("Error: La edad del alumno debe ser mayor o igual a 18 años y menor o igual a 100 años.")
            return

        if "@" not in email or "." not in email:
            print("Error: El email ingresado debe tener un formato válido (ejemplo: usuario@dominio.com)")
            return

        cursor.execute("INSERT INTO alumnos (nombre, apellido, edad, curso, email) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, edad, curso, email))
        conexion.commit()
        print("Alumno agregado exitosamente.")
        #cursor.excecute genera un insert para agregar un nuevo registro en la tabla alumnos, con los valores proporcionados por el usuario. Luego, conexion.commit() guarda los cambios en la base de datos.
        #commit agrega el registro a la base de datos, si no se hace commit, los cambios no se guardan y se pierden al cerrar la conexión.

    #los excepts se colocan en orden de especificidad, primero el más específico y luego el más general
    except ValueError:
        print("Error: La edad debe ser un número entero.")    
    except sqlite3.IntegrityError:
        print("Error: El emmail ingresado ya existe. Ingrese otro email.")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:    
        conexion.close()

def consultar_alumnos():
    conexion = sqlite3.connect("alumnos_talentotech.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos registrados.")
            return

        print("Lista de alumnos:")
        for alumno in alumnos:
            print(f"ID: {alumno[0]}, Nombre: {alumno[1]}, Apellido: {alumno[2]}, Edad: {alumno[3]}, Curso: {alumno[4]}, Email: {alumno[5]}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        conexion.close()

def buscar_alumno_por_id(id): 
    conexion = sqlite3.connect("alumnos_talentotech.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM alumnos WHERE id = ?", (id,))
        alumno = cursor.fetchone()

        if alumno is None:
            print(f"No se encontró un alumno con ID {id}.")
            return

        print(f"Alumno encontrado: ID: {alumno[0]}, Nombre: {alumno[1]}, Apellido: {alumno[2]}, Edad: {alumno[3]}, Curso: {alumno[4]}, Email: {alumno[5]}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        conexion.close()

def eliminar_alumno_por_id(id):
    conexion = sqlite3.connect("alumnos_talentotech.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("DELETE FROM alumnos WHERE id = ?", (id,))
        conexion.commit()

        if cursor.rowcount == 0:
            print(f"No se encontró un alumno con ID {id}.")
        else:
            print(f"Alumno con ID {id} eliminado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        conexion.close()

