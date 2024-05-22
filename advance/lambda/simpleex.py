lambdavalue = lambda a : a*2
print(lambdavalue(10))

##Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def abc(var1):
    return lambda lambdavar : lambdavar*var1

func = abc(2)
print(func(4))

