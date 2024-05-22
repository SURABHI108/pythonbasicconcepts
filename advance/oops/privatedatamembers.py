class xyz():
    def __init__(self,publicvar1,privatevar2): # consturctor
        self.publicvar = publicvar1
        self.__privatevar = privatevar2
    def display(self):
        print("public variable",self.publicvar)
        print("private variable",self.__privatevar)
    def __privatedispaly(self):
        print("i am private method of xyz class")

obj = xyz(2,3)
obj.display()
print("outside the class use public variable",obj.publicvar)
# print("outside the class use private variable",obj.__privatevar) # this will give error
# if we have to use it forcefully then we can use like
print("forcefully use private datamember of xyz class",obj._xyz__privatevar)
obj._xyz__privatedispaly() # forcefully used
