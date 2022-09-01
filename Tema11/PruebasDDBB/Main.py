from MyDatabase import *
import getpass

# Prácticas de ejercicios con DDBB
# Consulta a base de datos

def main():

    username = input("Nombre de usuario:")
    password = getpass.getpass("Contraseña:")

    if chekUser(username, password):
        print("Usuario correcto")
    else:
        print("Usuario incorrecto")


if __name__ == "__main__":
    main()
