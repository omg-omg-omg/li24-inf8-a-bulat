class User:
    def __init__(self, login, password, name, surname, age, role):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.age = age
        self.history_of_orders = []
        self.role = role
        #self.older_history = older_history

    def __str__(self):
        return "User"
