class person:
    var = 20 #class variable
    def __init__(self,name):
       self.name = name # object variable
    def display(self):
        print(self.name)
    def mainDisplay(self):
        self.display() # calling calss method from another method using self keyword
        
obj = person("surbhi")
obj.mainDisplay()
print(obj.var);
       
        