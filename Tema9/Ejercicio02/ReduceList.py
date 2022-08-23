def inputLista():

    inputValue = str(input("Indique lista de números separados por comas: ")).replace(" ", "").split(",")
    
    numInt = map(int, inputValue)
    numNones = filter(selectNones, numInt)
    
    return list(numNones)
        
def selectNones(n):
    if n % 2 == 0:
        return True
    
    return False

def sumReduce(n1, n2):

    return n1 + n2