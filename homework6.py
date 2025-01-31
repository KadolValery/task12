#task 1
words = ["apple", "banana", "kiwi", "cherry", "blueberry", "fig"]
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)

#task 2
words = ['apple', 'banana', 'cherry','aaaaaaaaaa ','date', 'fig', 'grape']
sorted_words = sorted(words, key=lambda word: word.count('a'))
print(sorted_words)

#task 3
school = {  '9а': 25, '9б': 30, '9в': 28, '9м': 22, '9ф': 26 }

school['9б'] = 32

school['9г'] = 27

del school['9ф']

total_students = sum(school.values())

print("Обновленный словарь классов и учащихся:", school)
print("Общее количество учащихся в 9 классах:", total_students)

#task 4
def phone_book():
    contacts = {}

    while True:
        entry = input()
        if entry == ".":
            break

        parts = entry.split()

        if len(parts) == 2:
            name, number = parts
            contacts[name] = number
        elif len(parts) == 1:
            name = parts[0]
            if name in contacts:
                print(contacts[name])
            else:
                print("не найдено")


phone_book()

#task 5
def get_element(lst: list, index: int):
    try:
        return lst[index]
    except IndexError:
        raise IndexError("Ошибка: индекс вне диапазона")

my_list = [10, 20, 30, 40, 50]

print(get_element(my_list, 2))

try:
    print(get_element(my_list, 10))
except IndexError as e:
    print(e)


