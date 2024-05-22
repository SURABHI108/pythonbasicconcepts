class Abc():
    def __iter__(self):
        self.count = 1
        return self
    def __next__(self):
        count = self.count
        if count <= 10:
            self.count += 1
            return count
        else:
            raise StopIteration

obj = Abc()
iterobj = iter(obj)

for i in iterobj:
  print("object = ",i)

# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));
# print(next(iterobj));