class Abc():        
    def dispaly(self):
        for i in range(0,10):
            yield i+1
            
objabc = Abc()
a = objabc.dispaly()
print(next(a))
print(next(a))

# class Abc():
    
#     def sq_numbers(self,n):
#         for i in range(1, n+1):
#             yield i*i


# obj = Abc()
# a = obj.sq_numbers(3)

# print("The square of numbers 1,2,3 are : ")
# print(next(a))
# print(next(a))
# print(next(a))