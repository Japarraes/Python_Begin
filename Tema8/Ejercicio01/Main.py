from Fichero import Fichero

def main():
    
    text = [
        "En un lugar de la mancha,",
        "de cuyo nombre no quiero acordarme,",
        "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,",
        "adarga antigua, ..."]

    # Crear fichero
    myFile = Fichero("MiFichero.txt", text)
    myFile.crearFile()
    myFile.readFile()


if __name__ == "__main__":
    main()
