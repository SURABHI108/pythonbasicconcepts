class Xyz:
    def __init__(self):
       print("xyz class")
       super(Xyz,self).__init__()
class Srh:
    def __init__(self):
        print("Srh class")
class Abc(Xyz,Srh):
    def __init__(self):
        super(Abc,self).__init__() # in multiple inheritance like that you can call all base class method 
        print("Abc class")

childobj = Abc()
