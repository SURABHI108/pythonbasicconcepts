def function1():
    print("hello world???")

function1()

## argument function
def function2(a):
    print(a)

function2("hiii")

## number of argumnets
def function3(*a):
    for i in range(len(a)):
        print(a[i])

function3("hii","hello","1")

## default parameter value
def function4(a=2):
    print(a)

function4("5767")
function4()
