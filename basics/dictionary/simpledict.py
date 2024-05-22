dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict1)
print(dict1["model"])

dict2 = dict(name = "surbhi" ,surname = "rank")
print(dict2)

print(dict2.get("name")) ## give same out put like dict2["name"]

print("keys of this dictionary",dict1.keys())
print("give value of dictionary",dict1.values())
print("The items() method will return each item in a dictionary, as tuples in a list :\n",dict1.items())