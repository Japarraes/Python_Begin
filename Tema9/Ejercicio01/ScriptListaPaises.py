def inputLista():

    paises = str(input("Indique paises separados por comas: ")).replace(" ", "").split(",")
        
    return list(set(paises))

def printLista(myList):

    lista  = sorted(myList)
    print(f"{list(lista)},")

