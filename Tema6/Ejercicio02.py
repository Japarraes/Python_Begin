# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
# que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
# sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:

    nombre = None
    nota = 0.0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirDatos (self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def estaAprobado(self):
        if (self.nota >= 5.0):
            return True
        else:
            return False

miAlumno = Alumno("Juan", 4.5)
miAlumno.imprimirDatos()
print("El alumno ", miAlumno.nombre, "está aprobado?: ", miAlumno.estaAprobado(), 
      "(", miAlumno.nota, ")")
