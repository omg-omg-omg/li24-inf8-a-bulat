class Information:
    def __init__(self, name, address, age, telephone_number):
        self.name = name
        self.adress = address
        self.age = age
        self.telephone_number = telephone_number

    def __str__(self):
        return "Information"


inf_1 = Information("Очевидно же, что это работает", "И делится информацией я не буду", 52, "+1 202-456-1111")
