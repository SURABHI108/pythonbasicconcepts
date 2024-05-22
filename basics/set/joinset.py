#The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c",1}
set2 = {1, 2, 3}
print(set1)
print(set2)

set3 = set1.union(set2)
print("after using union method ",set3)
print(set1 | set2) # union and | both are same

set4 = set2.difference(set1)
print("aftre using difference method",set4)
print(set2 - set1) #differences and - both giver same output

set5 = set2.intersection(set1)
print("after using intersection method",set5)
print(set2 & set1)# intersection and & both are same 