# square and cube every number in a given list of integers using Lambda.

list1 = [1,2,3,4,5,6,7,8,9]
print("original list",list1)

squer = list(map(lambda num : num**2,list1))
print("squer of aboven given numbers",squer)

qube = list(map(lambda num:num**3,list1))
print("qube of above given number",qube)