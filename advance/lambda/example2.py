# Write a Python program to sort a list of tuples using Lambda.

list_of_tuples = [('abc',1),('trp',4),('erd',2),('fgs',12)]
print("original list of tuples",list_of_tuples)

list_of_tuples.sort(key=lambda x:x[1])
print("sorted list of tuples",list_of_tuples)