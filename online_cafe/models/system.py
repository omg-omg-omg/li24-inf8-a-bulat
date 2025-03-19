from models import User
class FoodOrderingSystem:
    def __init__(self, users, ingredients, dishes, discount):
        self.cur_user = None
        self.users = users
        self.ingredients = ingredients
        self.dishes = dishes
        self.discount = discount

    def __str__(self):
        return "FoodOrderingSystem"
    # For Admins

    def add_ingredient(self, ingredient):
        if not self.cur_user.role == "Admin":
            return
        if ingredient not in self.ingredients:
            self.ingredients += [ingredient]

    def replenish_ingredient(self, name, quantity):
        if not self.cur_user.role == "Admin":
            return
        ingredient = next((ing for ing in self.ingredients if ing.name == name), None)
        if ingredient is None:
            return
        else:
            self.ingredients[ingredient].quantity += quantity

    def remove_ingredient(self, name):
        if not self.cur_user.role == "Admin":
            return
        ingredient = next((ing for ing in self.ingredients if ing.name == name), None)
        if ingredient is None:
            return
        else:
            self.ingredients.remove(ingredient)

    def add_dish(self, dish):
        if not self.cur_user.role == "Admin":
            return
        if dish not in self.dishes:
            self.dishes += [dish]

    def remove_dish(self, name):
        if not self.cur_user.role == "Admin":
            return
        dish = next((ing for ing in self.dishes if ing.name == name), None)
        if dish is None:
            return
        else:
            self.dishes.remove(dish)

    def add_discount(self, value):
        if not self.cur_user.role == "Admin":
            return
        if self.discount != 0.0 and value != 0.0:
            self.discount = value

    def change_discount(self, value):
        if not self.cur_user.role == "Admin":
            return
        if value != 0.0:
            self.discount = value

    def remove_discount(self):
        if not self.cur_user.role == "Admin":
            return
        self.discount = 0.0
    # For Users

    # def order(self, dishes, total_price, date):
        # order
    def sign_in(self, login, password):
        user = next((user for user in self.users if user.login == login), None)
        if user is None:
            return
        else:
            if password == user.password:
                self.cur_user = user

    def sign_up(self, login: str, password: str, name: str, surname: str, age: int):
        user = next((user for user in self.users if user.login == login), None)
        if user is None:
            user = User(login, password, name, surname, age, "User")
            self.users += [user]
            self.cur_user = user
        else:
            return
