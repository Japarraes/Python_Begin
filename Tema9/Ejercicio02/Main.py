from ReduceList import *
from functools import reduce

# tenéis que crear una aplicación que obtendrá los elementos impares de una lista
# pasada por parámetro con filter y realizará una suma de todos estos elementos 
# obtenidos mediante reduce.
def main():

    noneNum = inputLista()
    print(f"La suma es: {reduce(sumReduce, noneNum)}")
    


if __name__ == "__main__":
    main()
