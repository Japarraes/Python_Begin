import sqlite3

def InsertStudent(id, nombre, apellidos):

    # Abrir base de datos y cursor
    conn = sqlite3.connect("misalumnos.db")
    cursor = conn.cursor()

    # Consultas a la base de datos
    query = '''INSERT INTO alumnos (id, name, surname) VALUES(?, ?, ?)'''
    cursor.execute(query, (id, nombre, apellidos))
    conn.commit()

    # Cerrar cursor y base de datos al terminar
    cursor.close
    conn.close

def ShowStudent(nombre):

    # Abrir base de datos y cursor
    conn = sqlite3.connect("misalumnos.db")
    cursor = conn.cursor()

    # Consultas a la base de datos
    
    query = f"SELECT * FROM alumnos WHERE name = '{nombre}'"
    
    rows = cursor.execute(query)
    
    for row in rows:
        print(f"ID: {row[0]}, Nombre: {row[1]}, Apellidos: {row[2]}")
    
        # Cerrar cursor y base de datos al terminar
    cursor.close
    conn.close