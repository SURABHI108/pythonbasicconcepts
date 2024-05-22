class xyz():
    numOfObject = 0
    def __init__(self,name): # consturctor
        self.name = name
        xyz.numOfObject += 1
        print("created object",self.name)
        print("total object",xyz.numOfObject)
    def __del__(self):  # destructor
        xyz.numOfObject -= 1
        print(self.name)

obj1 = xyz("object1")
obj2 = xyz("object2")
obj3 = xyz("object3")
obj4 = xyz("object4")

del obj2