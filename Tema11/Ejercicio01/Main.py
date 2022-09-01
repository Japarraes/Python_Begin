from AlumnosDDBB import *

# Crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, 
# la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

def main():

    InsertStudent(1, "Juan", "García")
    InsertStudent(2, "Alberto", "Doblas")
    InsertStudent(3, "Marina", "Pérez")
    InsertStudent(4, "Miriam", "Ramírez")
    InsertStudent(5, "Manuel", "Alvarez")
    InsertStudent(6, "Francisco", "González")
    InsertStudent(7, "Pedro", "Moreno")
    InsertStudent(8, "Teresa", "Sánchez")

    ShowStudent("Teresa")

if __name__ == "__main__":
    main()
