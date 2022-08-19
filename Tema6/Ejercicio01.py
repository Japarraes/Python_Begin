# Tema6 - Ejercicio 1
# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# - Color
# - Ruedas
# - Puertas
# 
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# - Velocidad
# - Cilindrada
#
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

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

miCoche = Coche("Blaco", 4, 5, 120, 2.0)

print("Color: ", miCoche.color)
print("ruedas: ", miCoche.ruedas)
print("Puertas: ", miCoche.puertas)
print("Velocidad: ", miCoche.velocidad)
print("Cilindrada: ", miCoche.cilindrada)