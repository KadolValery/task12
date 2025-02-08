#
# class Task1Class:
#     def __init__(self, first_number, second_number):
#         self.first_number = first_number
#         self.second_number = second_number
#
#
#     def print_func(self):
#         print(f"First number: {self.first_number} Second number: {self.second_number}")
#
#     def change_variables(self, new_var1, new_var2):
#         self.first_number = new_var1
#         self.second_number = new_var2
#         print(new_var1, new_var2)
#
#     def sum_func(self):
#         print(f"Sum of {self.first_number} and {self.second_number} = {self.first_number + self.second_number}")
#
#     def max_func(self):
#         print(max(self.first_number, self.second_number))
#
#
#
# num = Task1Class(first_number=10, second_number=20)
# num.print_func()
# num.change_variables(15, 25)
# num.sum_func()
# num.max_func()


#task 2
# class DecimalCounter:
#     def __init__(self, min_value, max_value, initial_value ):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.initial_value = initial_value
#
#         if not (self.min_value <= self.initial_value <= self.max_value):
#             raise ValueError(f"Начальное значение должно быть в диапазоне [{self.min_value}, {self.max_value}]")
#
#
#     def increase_value(self):
#         if self.max_value > self.initial_value:
#             for i in range(self.initial_value ,self.max_value - 1):
#                 self.initial_value += 1
#                 print(self.initial_value)
#         else:
#             print("Value is max")
#
#     def decrease_value(self):
#         if self.min_value < self.initial_value:
#             while self.min_value + 1 < self.initial_value:
#                 self.initial_value -= 1
#                 print(self.initial_value)
#         else:
#             print("Value is min")
#
#     def get_value(self):
#         print(f"Текущее значение {self.initial_value}")
#
# val = DecimalCounter(min_value=2, max_value=10, initial_value=7)
# val.increase_value()
# val.decrease_value()
# val.get_value()


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        if name in self.products:
            print(f'Продукт "{name}" уже существует в магазине.')
        else:
            self.products[name] = price
            print(f'Продукт "{name}" добавлен в магазин по цене ${price:.2f}.')

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f'Продукт "{name}" удален из магазина.')
        else:
            print(f'Продукт с названием "{name}" не найден.')

    def search_product(self, name):
        found_products = {k: v for k, v in self.products.items() if name.lower() in k.lower()}
        if found_products:
            print("Найденные продукты:")
            for product_name, price in found_products.items():
                print(f"{product_name} - ${price:.2f}")
        else:
            print(f'Продукты с названием "{name}" не найдены.')

    def list_products(self):
        if self.products:
            print("Список продуктов в магазине:")
            for product_name, price in self.products.items():
                print(f"{product_name} - ${price:.2f}")
        else:
            print("Магазин пуст.")


# Пример использования класса Shop
shop = Shop()

# Добавление продуктов
shop.add_product("Яблоко", 0.5)
shop.add_product("Банан", 0.3)
shop.add_product("Апельсин", 0.7)

# Список всех продуктов
shop.list_products()

# Поиск продукта
shop.search_product("яблоко")

# Удаление продукта
shop.remove_product("Банан")

# Список продуктов после удаления
shop.list_products()