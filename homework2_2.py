#task 9
from math import factorial
from turtledemo.penrose import start

number_1 = 10
for i in range(20):
     print(number_1)

#TASK 10
start_num = int(input("Enter a number: "))
stop_num = int(input("Enter a number: "))
for n in range(start_num, stop_num+1):
    print(n)

#task 12
sum_t12 = 0
for y in range(100, 501):
    sum_t12 = sum_t12 + y
    print(sum_t12)

print("\n")
#task 13
num_t13 = 1
for k in range(5, 21):
    num_t13 = num_t13 * k
    print(num_t13)

#task 14
num_t14 = int(input("Enter a number: "))
fact = 1
for r in range(2, num_t14+1):
    fact = fact * r
    print(fact)
