import pickle

class Vehiculo:

    color = None
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):

    velocidad = 0
    cilindrada = 0.0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def toString(self):
        print("Color: ", self.color)
        print("ruedas: ", self.ruedas)
        print("Puertas: ", self.puertas)
        print("Velocidad: ", self.velocidad)
        print("Cilindrada: ", self.cilindrada)
    



