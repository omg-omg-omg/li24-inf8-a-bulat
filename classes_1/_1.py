class Pet:
	def __init__(self, name, animal_type, age):
		self.name = name
		self.animal_type = animal_type
		self.age = age
		
	def __str__():
		return "Pet"
		
	def set_name(self, name):
		self.name = name
		
	def set_animal_type(self, animal_type):
		self.animal_type = animal_type
		
	def set_age(self, age):
		self.age = age
		
	def get_name(self):
		return self.name
		
	def get_animal_type(self):
		return self.animal_type
		
	def get_age(self):
		return self.age
		
		
your_pet = Pet(input("Имя"), input("Тип животного"), int(input("Возраст")))
print(your_pet.get_name())
print(your_pet.get_animal_type())
print(your_pet.get_age())
