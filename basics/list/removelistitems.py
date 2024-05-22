list = ["cat","dog","lion","elephant","tiger","crocodial"]

print(list)
list.remove("tiger")
print("after remove",list)

list.pop(1)
print(list)

del list[3]
print(list)

#The clear() method empties the list. The list still remains, but it has no content.
list.clear()
print("after clear the list",list)

