import array as arr 

numbers = arr.array('i',[1,2,3,4])
print("original array",numbers)
revers_numbers = numbers[::-1]
numbers.reverse()
print(revers_numbers)
print("reverse array",numbers)
