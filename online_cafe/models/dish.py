class Dish:
    def __init__(self, name, description, ingredients, price):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return "Dish"
