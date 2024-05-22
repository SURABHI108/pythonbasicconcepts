import array as arr 

numbers = arr.array('i',[1,2,3,4])
print("original array",numbers)
numbers.remove(1)
numbers.pop(0)
print("after adding value ",numbers)

