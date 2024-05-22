import complisteleaccesscomponent

class Custom():
    def display(self):
        print("hello i am custom class")
        
complex_list = [1,"hello",[2,3,4],("tuple",2),{"key":"value"},{"nested_list":[5,6,7]},{"nesteddict":{"a":9,"b":10}},{"customobj":Custom()}]

complisteleaccesscomponent.elementAccess(complex_list,Custom)

# print(complex_list[5]["nested_list"][2])
# print(complex_list[6]["nesteddict"]["a"])
# print(complex_list[-1]["customobj"].display())
# for element in complex_list:
#     print(element)


            
