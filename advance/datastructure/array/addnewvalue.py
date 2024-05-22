import array as arr 

numbers = arr.array('i',[1,2,3,4])
print("original array",numbers)
numbers.append(23)
numbers.insert(2,45)
print("after adding value ",numbers)
numbers.extend([10,20,30,40])
print("after adding value ",numbers)

