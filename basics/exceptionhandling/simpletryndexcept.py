a = int(input("enter numenorator : "))
b = int(input("enter denomenorator : "))
try:
    quo = a/b
    print("quotient",quo);
except ZeroDivisionError:
    print("not valid value of denominator")