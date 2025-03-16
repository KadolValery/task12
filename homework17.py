import re


# strings = [
#     "The cat is on the roof.",
#     "Dogs are great pets.",
#     "I have a cat and a dog.",
#     "Cats are independent animals.",
#     "This string does not contain the keyword."
# ]
#
#
# pattern = r'cat'
#
#
# for string in strings:
#     if re.search(pattern, string):
#         print(string)

        #task2

# strings = [
#     "z123z.",
#     "zabcde.",
#     "zxyzt.",
#     "z123z",
#     "Nz213z",
#     "z12z."
# ]
#
#
# pattern = r'z.{3}z'
#
#
# for string in strings:
#     if re.search(pattern, string):
#         print(string)


#task 4


# text = "Это пример строки, где есть несколько слов, начинающихся на гласные буквы ."
#
# pattern = r'\b[аеёиоуыэюяАЕЁИОУЫЭЮЯ]w*'
#
# matches = re.findall(pattern, text)
#
# print("Слова, начинающиеся на гласную букву:")
# for word in matches:
#     print(word)

# lines = [
#     "The human brain is fascinating.",
#     "Humans and computers can work together.",
#     "Every human has unique qualities.",
#     "The future is about human-computer interaction."
# ]
#
# #
# modified_lines = [re.sub(r'human', 'computer', line) for line in lines]
#
#
# print("Полученные строки:")
# for modified_line in modified_lines:
#     print(modified_line)




# text = "This is a sample text with some words like bubble, apple, and banana."
#
# words_with_b = re.findall(r'\b[^ ]*b[^ ]*\b', text)
#
#
# print("Слова с буквой 'b':", words_with_b)

# phone_numbers = [
#     "9123456789",
#     "8123456789",
#     "7123456789",
#     "91234",
#     "9876543210",
#     "1234567890",
#     "81234567890",
# ]
#
# pattern = r'^[89]d{9}$'
#
# valid_numbers = [number for number in phone_numbers if re.fullmatch(pattern, number)]
#
# print(valid_numbers)

text = "15-03-2023"


pattern = r'\b(d{2})-(d{2})-(d{4})\b'


match = re.search(pattern, text)

if match:
    date = match.group(0)
    print("Найдена дата:", date)
else:
    print("Дата не найдена.")