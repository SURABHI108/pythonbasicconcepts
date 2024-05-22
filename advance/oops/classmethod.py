class person():
    def __init__(self,val) :
       self.val = val
    def display(self):
        print(self.val)
    @classmethod
    def classmethod(cls,val):
        return cls(val)

pbj1 = person.classmethod(23)

    