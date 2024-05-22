def abc(var1):
    def xyz(var2):
        return var1+var2
    return xyz

obj_fun =  abc(3)
print(obj_fun(4))