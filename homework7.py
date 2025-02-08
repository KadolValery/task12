import json
import os
import math
from datetime import datetime, timedelta

# numbers = []
#
# for i in range(10):
#     numbers.append(int(input("enter a number: ")))
#
# with open('input.txt', 'w') as file:
#     file.write(' '.join(map(str, numbers)))
#
#
# #task 2
# with open('input.txt', 'r') as file:
#     data = list(map(int, file.read().split()))
#     data = int(math.prod(data))
#
#
# with open('output.txt', 'w') as file:
#     file.write(str(data))
#
# #task 3
# with open('products.json', 'r', encoding='utf-8') as json_file:
#     products = json.load(json_file)
#
#
# current_date = datetime.now()
#
#
# filtered_products = []
#
# for product in products:
#     total_price = product['quantity'] * product['price_per_unit']
#     arrival_date = datetime.strptime(product['arrival_date'], "%Y-%m-%d")
#
#     if total_price > 1000000 and (current_date - arrival_date) > timedelta(days=30):
#         filtered_products.append(product)
#
# # Вывод отфильтрованных товаров
# print("Товары, хранящиеся больше месяца и стоимость которых превышает 1 000 000 р:")
# for product in filtered_products:
#     print(f"Название: {product['name']}, Количество: {product['quantity']}, "
#           f"Цена за единицу: {product['price_per_unit']}, "
#           f"Дата поступления: {product['arrival_date']}")



# #task 5
#
# with open('questions.txt', 'r', encoding='utf-8') as questions_file:
#     questions = questions_file.readlines()
#
# with open('answers.txt', 'r', encoding='utf-8') as answers_file:
#     answers = answers_file.readlines()
#
#
# questions = [question.strip() for question in questions]
# answers = [answer.strip() for answer in answers]
#
# score = 0
#
#
# for i in range(len(questions)):
#     print(f"Вопрос {i + 1}: {questions[i]}")
#     user_answer = input("Ваш ответ: ")
#
#
#     if user_answer.lower() == answers[i].lower():
#         print("Верно!")
#         score += 1
#     else:
#         print(f"Неверно! Правильный ответ: {answers[i]}")
#
#
# print(f"\nВы ответили правильно на {score} из {len(questions)} вопросов.")

#task 6
data = {
    10001: ("Alice", 30),
    10002: ("Bob", 25),
    10003: ("Charlie", 35),
    10004: ("David", 28),
    10005: ("Eva", 22),
    10006: ("Frank", 40)
}

task6_lst = list(data)

with open('data.json', 'w') as outfile:
    for key, value in data.items():
        json.dump({key: value}, outfile)
        outfile.write('\n')


