#task 1
number = int(input("Enter a number: "))
value = 1
while  value**2 < number:
    print(value**2, end= ' ')
    value += 1

#task 2
print("\n")
num_t2 = int(input("Enter a number for task 2: "))
while num_t2 > 9:
    num_t2 = num_t2 // 10

print(num_t2, "\n")

#task 3
num_t3 = int(input("Enter a number for task 3: "))
value_t3 = num_t3%10
num_t3 = num_t3 // 10
while num_t3 > 0:
    if num_t3 % 10 > value_t3:
        value_t3 = num_t3 % 10
    num_t3 = num_t3 // 10
print(value_t3, "\n")

#task 4

any_string = 'asdfghjkl'
print(any_string[2])
print(any_string[-2])
print(any_string[:5])
print(any_string[:-2])
print(any_string[::2])
print(any_string[1::2])
print(any_string[::-1])
print(len(any_string))

#task 5
#task5_string = 'Hello world'
#word = task5_string.split(' ')
#new_string = task5_string[1] + " " + task5_string[0]
#print(new_string)

# task 6

task6_string = 'allar'
print(task6_string == task6_string[::-1] )

#task 8
first_list = [5, 6, 2, 7, 11, 65]
second_list = [6, 7, 114, 54, 3]
third_list = []
for num1 in first_list:
    for num2 in second_list:
        if num1==num2:
            third_list.append(num1)
            break

first_list=list(set(first_list)-set(third_list))
print(min(list(set(first_list))))




