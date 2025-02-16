# class BankAccount:
#     def __init__(self, balance:float = 0):
#         self.__balance = balance
#         self.daily_limit = 5000
#         self.withdrawals_today = 0
#         self.max_withdrawals = 3
#
#     def deposit(self, amount: float):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Пополнено на {amount}. Текущий баланс: {self.__balance}")
#         else:
#             print("Сумма пополнения должна быть положительной.")
#
#     def withdraw(self, amount: float):
#         if self.withdrawals_today >= self.max_withdrawals:
#             print("Достигнут лимит на количество снятий в день.")
#             return
#
#         if amount > self.__balance:
#             print("Недостаточно средств на счете.")
#             return
#
#         if amount > self.daily_limit:
#             print(f"Сумма снятия превышает суточный лимит в {self.daily_limit}.")
#             return
#
#         self.__balance -= amount
#         self.withdrawals_today += 1
#         print(f"Снято {amount}. Текущий баланс: {self.__balance}")
#
#     def get_balance(self):
#         return self.__balance
#
#
# bank_account = BankAccount()
# bank_account.deposit(3000)
# bank_account.deposit(3000)
# bank_account.deposit(3000)
#
# bank_account.withdraw(1000)
# bank_account.withdraw(1000)
# bank_account.withdraw(1000)
# bank_account.withdraw(1000)
#
# bank_account.get_balance()

# import random
# import time
#
# class Animal:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.hunger = 100  # 100 - сыт, 0 - голоден
#
#     def make_sound(self):
#         pass
#
#     def eat(self, food: int):
#         self.hunger = min(100, self.hunger + food)
#         print(f"{self.name} поел. Уровень сытости: {self.hunger}")
#
#     def pass_time(self):
#         self.hunger -= random.randint(5, 15)
#         if self.hunger < 0:
#             self.hunger = 0
#
#
# class Lion(Animal):
#     def make_sound(self):
#         print("Ррррр")
#
#     def hunt(self):
#         print(f"{self.name} охотится!")
#
#
# class Elephant(Animal):
#     def make_sound(self):
#         print("Туууу")
#     def trumpet(self):
#         print(f"{self.name} издает звук трубления!")
#
#
# class Penguin(Animal):
#     def make_sound(self):
#         print("ПщПщПщ")
#
#     def swim(self):
#         print(f"{self.name} плывет!")
#
#
#
# lion = Lion("Лев", 5)
# elephant = Elephant("Слон",10)
# penguin = Penguin("Пингвин",4)
#
# lion.make_sound()
# elephant.make_sound()
# penguin.make_sound()
#
# for day in range(1,4):
#     print(f"\nДень {day}:")
#
#     for animal in [lion, elephant, penguin]:
#         animal.pass_time()
#         if animal.hunger < 70:
#             print(f"{animal.name} голоден! Уровень сытости: {animal.hunger}")
#             animal.eat(30)  # Кормим животное
#         else:
#             print(f"{animal.name} не голоден. Уровень сытости: {animal.hunger}")

class Temperature:
    def __init__(self, _celsius: float):
        self._celsius = None
        self.celsius = _celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C")
        self._celsius = value


    @property
    def fahrenheit(self) -> float:
       return (self._celsius * 1.8) + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

temp=Temperature(40)

print(f"Температура в Цельсиях: {temp.celsius}°C")
print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")
print(f"Температура в Кельвинах: {temp.kelvin} K")
temp.celsius = -200
print(f"Температура в Цельсиях: {temp.celsius}°C")
print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")
print(f"Температура в Кельвинах: {temp.kelvin} K")