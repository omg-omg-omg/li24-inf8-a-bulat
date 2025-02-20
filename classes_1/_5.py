class Ingredient:
    def __init__(self, name, type_of_product, price):
        self.name = name
        self.type_of_product = type_of_product
        self.price = price

    def __str__(self):
        return "Ingredient"


class Recipe:
    def __init__(self, name, list_of_ingredients, quantity):
        self.name = name
        self.list_of_ingredients = list_of_ingredients
        self.quantity = quantity

    def __str__(self):
        return "Recipe"

    def show_ingredients(self):
        return self.list_of_ingredients

    def get_price(self):
        price = 0
        for i in range(len(self.list_of_ingredients)):
            for j in range(self.quantity[i]):
                price += self.list_of_ingredients[i].price
        return price


class Menu:
    def __init__(self, menu):
        self.menu = menu

    def __str__(self):
        return "Menu"

    def show_menu(self):
        print(str(" " * 8) + "МЕНЮ" + str(" " * 8))
        for i in self.menu:
            print(i.name + str("." * (20 - len(i.name) - len(str(i.get_price())))) + str(i.get_price()))


ingredient_potato = Ingredient("Картошка", "Съедобное", 52)
recipe_bulba = Recipe("Бульба", [ingredient_potato], [2])
_1 = Menu([recipe_bulba])
_1.show_menu()
# Вроде работает
