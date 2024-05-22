cube = lambda x: x ** 3

# Define the function to generate the first n Fibonacci numbers
def fibonacci(n):
    fib_list = []  # Initialize an empty list
    if n >= 1:
        fib_list.append(0)  # Add the first Fibonacci number if n >= 1
    if n >= 2:
        fib_list.append(1)  # Add the second Fibonacci number if n >= 2
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])  # Add the next Fibonacci number
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) 
    
    ## The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.