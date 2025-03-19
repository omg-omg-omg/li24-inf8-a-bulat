import sys

from models import *
# from console import *
system = FoodOrderingSystem([User("Login", "12345678", "Name", "Surname", 52, "Admin")],
                            [Ingredient("Ingredient", 5)],
                            [Dish("Dish", "Simple dish!", ["Ingredient"], 52.0)],
                            0)


def log_manager():
    print("""Это Онлайн Кафе. Добро пожаловать!
    1. Войти
    2. Зарегистрироваться
    3. Выйти""")
    match input():
        case "1":
            system.sign_in(input("Введите ваш логин"), input("Введите ваш пароль"))
            print("Вход успешно пройден")
        case "2":
            system.sign_up(input("Введите ваш логин"), input("Введите ваш пароль"), input("Введите ваше имя"),
                           input("Введите вашу фамилию"), int(input("Введите ваш возраст")))
            print("Регистрация успешно пройдена")
        case "3":
            print("Пока")
            sys.exit()
    print("Добро пожаловать в систему!")
    print("- Помощь")


log_manager()
while True:
    match input():
        case "Помощь":
            print("""- Добавить ингредиент
- Пополнить ингредиент
- Удалить ингредиент
- Добавить блюдо
- Удалить блюдо
- Добавить скидку
- Поменять скидку
- Удалить скидку
""")
        case "Добавить ингредиент":
            system.add_ingredient(Ingredient(input("Введите название ингредиента"), int(input("Введите количество"))))
        case "Пополнить ингредиент":
            system.replenish_ingredient(input("Введите название ингредиента"), int(input("Введите количество")))
        case "Удалить ингредиент":
            system.remove_ingredient(input("Введите название ингредиента"))
        case "Добавить блюдо":
            system.add_dish(Dish(input("Введите название блюда"), input("Введите описание блюда"),
                                 input("Введите названия продуктов").split(", "), float(input("Введите цену"))))
        case "Удалить блюдо":
            system.remove_dish(input("Введите название блюда"))
        case "Добавить скидку":
            system.add_discount(float(input("Введите скидку в процентах")))
        case "Поменять скидку":
            system.change_discount(float(input("Введите скидку в процентах")))
        case "Удалить скидку":
            system.remove_discount()
        case "Посмотреть историю заказов":
            for i in range(1, len(system.cur_user.history_of_orders) + 1):
                print(i, system.cur_user.history_of_orders[i])
        case "Заказать":
            print("........Меню........")
            for i in system.dishes:
                print((("." * ((20 - len(i.name) - len(str(i.price))) // 2)) + i.name + str(i.price) +
                       ("." * ((20 - len(i.name) - len(str(i.price)) + 1) // 2))))
        case "Выйти":
            system.cur_user = None
            log_manager()

# Это можно было сделать намного легче, но мне лень
