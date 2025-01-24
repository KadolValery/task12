import math

first_num = int(input("Enter first number: "))
second_num =  int(input("Enter second number: "))

def minimum_func(first, second, *args):
    return print(min(first, second, *args))
#task 1
minimum_func(first_num, second_num)
#task 2
minimum_func(first_num,second_num, 4, 5)

#task 3
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))

def distance(x1, y1, x2, y2):
    return print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

distance(x1, y1, x2, y2)

#task 4
number = int(input("Enter number: "))

def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(prime_num(number))

#task 5

fibonacci_num = int(input("Enter fibonacci number: "))


#def fibonacci(num):
#    fib1 = 1
#    fib2 = 1
#    i = 0
#    while i < num-2:
#       sum = fib1 + fib2
#        fib1 = fib2
#        fib2 = sum
#        i += 1

#    return fib2

#print(fibonacci(number))




#print(fibonacci(number))



