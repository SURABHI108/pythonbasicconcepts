try:
    a = int(input("enter any number"))
    print(a)
except (ValueError):
    print("please enter true value")
else:
    print("your given value is currect")
    