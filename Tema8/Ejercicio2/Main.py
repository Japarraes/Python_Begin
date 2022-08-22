from PickleObject import PickleObject
from Vehiculo import Coche

def main():

    miCoche = Coche("Blaco", 4, 5, 120, 2.0)
    PickleObject.seriarObjeto("MiObjeto.bin", miCoche)
    
    newCoche = PickleObject.deSeriarObjeto("MiObjeto.bin")
    print(newCoche.toString())


if __name__ == "__main__":
    main()
