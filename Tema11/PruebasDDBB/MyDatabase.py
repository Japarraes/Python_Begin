import sqlite3

def chekUser(user, pasw):

    # Abrir base de datos y cursor
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    # Consultas a la base de datos
    query = f"SELECT * FROM users WHERE username = '{user}' AND password='{pasw}'"
    rows = cursor.execute(query)

    # Cerrar cursor y base de datos al terminar
    cursor.close
    conn.close

    if rows == None:
        return False
    else:
        return True

def InsertUser(id, user, pasw):

    # Abrir base de datos y cursor
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    # Consultas a la base de datos
    query = '''INSERT INTO users (id, username, password) VALUES(?, ?, ?)'''
    cursor.execute(query, (id, user, pasw  ))
    conn.commit()

    # Cerrar cursor y base de datos al terminar
    cursor.close
    conn.close

   