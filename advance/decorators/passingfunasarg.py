def sum(var1,var2):
    return var1 + var2
def sub(var1,var2):
    return var1-var2
def mainfunc(func):
    mainfunc = func(4,2)
    return mainfunc

print(mainfunc(sum))
print(mainfunc(sub))