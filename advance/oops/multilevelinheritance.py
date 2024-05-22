class Xyz:
    def __init__(self):
       print("xyz class")
class Srh(Xyz):
    def __init__(self):
        super().__init__()
        print("Srh class")
class Abc(Srh):
    def __init__(self): 
        super().__init__()
        print("Abc class")

obj1 = Abc()