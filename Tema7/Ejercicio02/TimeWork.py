"""
Script que indica si es la hora de ir a casa en función de la hora fin de jornada pasada por parámetro
En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""
import time

def goHome(finWork):
 
    fecha = time.localtime()
    if (fecha.tm_hour >= finWork):  # Si son las 7:00 pm o superior, mostrar mensaje de irse a casa
        print("Es hora de irse a casa")
    else:
        horaRes = finWork - fecha.tm_hour
        minRes = 60 - fecha.tm_min
        secRes = 60 - fecha.tm_sec
        print("Te quedan:", horaRes, "h", minRes, "min", secRes, "sec. para poder ir a casa")

