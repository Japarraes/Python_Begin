class Fichero:

    f = None
    path = None
    lines = None
    
    def __init__(self, path, lines):
        self.path = path
        self.lines = lines

    def crearFile(self):

        self.f = open(self.path, "w")

        for line in self.lines:
            if not line.endswith("\n"):
                line +="\n"
            
            self.f.write(line)
            

        self.f.close

    def readFile(self):
        self.f = open(self.path, "r")
        
        text = self.f.readlines()

        self.f.close
        
        for line in text:
            if not line.endswith("\n"):
                line += "\n"
            
            print(f"{line}")

        

