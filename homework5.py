#task 1


odd_numbers = [n for n in range(10, 100) if n %2==1]
print(odd_numbers)

#task 2
any_lst = [i**2 for i in range(1, 11)]
print(any_lst)

#task 3
task3_lst = [j for j in range(100, 1000) if j % 5 == 0 or j % 3 == 0]
print(task3_lst)

#task 4
first_numb, second_numb, third_numb = map(int, input("Enter 3 numbers:").split())
task4_lst = [k ** third_numb for k in range(first_numb, second_numb+1)]
print(task4_lst)

#task5
input_numbers = input("Enter numbers: ")
numbers = input_numbers.split()
filtered_numbers = list(filter(lambda num: '0' in num, numbers))
print("Numbers containing 0:", filtered_numbers)

#task 6

words = ["apple", "banana", "cherry", "avocado", "grape", "anaconda", "kiwi",]
filtered_words = list(filter(lambda word: word.count('a') > 2, words))
print(filtered_words)

#task 7
strings = ["hello", "world", "python", "programming"]
uppercase_str = list(map(lambda s: s.upper(), strings))
print(uppercase_str)

#task 8
strs = ["hello123", "world456", "pyth0n", "programming789", "teacmeski11s"]
no_digits_strings = list(map(lambda s: ''.join(filter(lambda char: not char.isdigit(), s)), strs))
print(no_digits_strings)