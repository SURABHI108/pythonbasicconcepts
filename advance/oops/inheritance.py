# class Xyz:
#     def __init__(self,var1,var2):
#         self.var1= var1
#         self.var2 = var2
#     def display(self):
#         print("parent class var1",self.var1)
#         print("parent class var2",self.var2)
# class Abc(Xyz):
#     pass # if child bod empty then simply you have to write pass

# childobj = Abc(1,2)
# childobj.display()

## using super() method you can call parent class method inside child method

class Xyz:
    def __init__(self,var1,var2):
        self.var1= var1
        self.var2 = var2
    def display(self):
        print("parent class var1",self.var1)
        print("parent class var2",self.var2)
class Abc(Xyz):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        super().__init__(var1, var2)
    def display(self):
        super().display()
        print("child class data",self.var2)
    
# parentobj = Xyz(6,7)
# parentobj.display()
childobj2 = Abc(4,5)
childobj2.display()    

