def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
 
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
 
@decor1
@decor
def num(): 
    return 20
 
@decor
@decor1
def num2():
    return 30
   
print(num()) 
print(num2())