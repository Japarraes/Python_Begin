import pickle

class PickleObject:

    myObject = None
    myFile = None

    def __init__(self) -> None:
        pass
        
    def seriarObjeto(file, Object):
        myFile = open(file, "wb")
        pickle.dump(Object, myFile)
        myFile.close()

    def deSeriarObjeto(file):
        myFile = open(file, "rb")
        myObject = pickle.load(myFile)
        return myObject
        