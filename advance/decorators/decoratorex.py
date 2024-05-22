def abc(func):
    def xyz():
        print("helloo")
        func()
        print("finished") 
    return xyz

def outerfunc():
    print("i am outer function")

obj = abc(outerfunc)
obj()
