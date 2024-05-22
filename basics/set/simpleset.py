a = {"apple", "banana", "cherry", False, True, 0}
print(a)

print(len(a))

# add set item

a.add("dog")
print("after adde new item\n",a)

# merge to set using update method
b = {"hello","how","are","you"}
a.update(b)
print(a)

## remove set item sem like list methods 