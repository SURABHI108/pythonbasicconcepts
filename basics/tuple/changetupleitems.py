a = (1,2,3,4,54,56,32)
print(a)

a = list(a) # tupple is unchangable so for the chage of tuple item we have to first convert it into list nd chage same like list
print(a)
a[1] = "hii"
a.append("orange")

a = tuple(a) # convert list to tuple
print("after changing",a)
