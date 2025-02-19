class Employee:
    def __init__(self, name, identification_number, department, job_title):
        self.name = name
        self.identification_number = identification_number
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return "Employee"


_1 = Employee("Марат Маратыч", 47899, "Бухгалтерия", "Вице-президент")
_2 = Employee("Минуллин Надир", 39119, "ИТ-отдел", "Программист-инженер")
_3 = Employee("Криштиану Роналду", 81774, "Уборка помещений", "Уборщица")
# Даже не уборщик
print(_1.name, _1.identification_number, _1.department, _1.job_title)
print(_2.name, _2.identification_number, _2.department, _2.job_title)
print(_3.name, _3.identification_number, _3.department, _3.job_title)
