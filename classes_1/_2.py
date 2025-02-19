class Car:
    def __init__(self, year, producer, speed):
        self.year = year
        self.producer = producer
        self.speed = speed

    def __str__(self):
        return "Car"

    def accelerate(self):
        self.speed += 5

    def break_(self): #Назвать "break"-ом невозможно! 
        self.speed -= 5

    def get_speed(self):
        return self.speed


my_car = Car(2020, "Tesla", 60)
for i in range(5):
    my_car.accelerate()
    print(my_car.get_speed())
for i in range(5):
    my_car.break_()
    print(my_car.get_speed())
