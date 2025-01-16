#Task 1
print("Task 1:")
a = 13
if a%10 == 3:
    print("True","\n")
else:
    print("False","\n")

#Task 2
num_1, num_2, num_3 = map(int, input("enter 3 numbers").split())
print(num_1, num_2, num_3)
if num_1<0 or num_2<0 or num_3<0:
    print("True","\n")
else:
    print("False","\n")

#Task 3
if num_1%2==0 and num_2%2==0 or num_1%2==1 and num_2%2==1:
    print("True","\n")
else:
    print("False","\n")

#Task 4
side_1 ,side_2, side_3 = map(int, input("enter 3 sides").split())
if side_1==side_2==side_3:
    print("equilateral")
elif side_1==side_2 or side_1==side_3 or side_2==side_3:
    print("isosceles")
else:
    print("scalene")


#task 5
n_1, n_2, n_3 = map(int, input("enter 3 numbers").split())
if n_1%2==0 and n_2%2==0 and n_3%2==0:
    print("3 number is even")
elif n_1%2==0 and n_2%2==0 and n_3%2==1 or n_2%2==0 and n_3%2==0 or n_1%2==1 or n_3%2==0 and n_1%2==0 and n_2%2==1:
    print("2 number is even")
else: print("1 number is even")

#task 6

num_6_t6 = int(input("enter number"))

if (num_6_t6/10 + num_6_t6%10)>9:
    print("true")
else:
    print("false")

#task 7
    n = input()
    n1 = n[0]
    n2 = n[1]
    n3 = n[2]
    n4 = n[3]
    if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
        print("true ")
    else:
        print("false")