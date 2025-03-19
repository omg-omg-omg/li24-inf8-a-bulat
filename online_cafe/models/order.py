class Order:
    def __init__(self, dishes, total_price, date):
        self.dishes = dishes
        self.total_price = total_price
        self.date = date

    def __str__(self):
        return "Order"
