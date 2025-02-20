class Question:
    def __init__(self, q, a1, a2, a3, a4, true_answer):
        self.q = q
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.true_answer = true_answer

    def __str__(self):
        return "Question"

# Решил сделать удобнее


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def __str__(self):
        return "Quiz"

    def start_game(self):
        points = 0
        for i in range(1, len(self.questions) + 1):
            print(f"№{i} - {self.questions[i - 1].q}")
            print(self.questions[i - 1].a1)
            print(self.questions[i - 1].a2)
            print(self.questions[i - 1].a3)
            print(self.questions[i - 1].a4)
            answer = input("Введите номер ответа")
            while len(answer) != 1 or str(answer) not in "1234":
                answer = input("Введите номер ответа")
            if int(answer) == self.questions[i - 1].true_answer:
                print("Правильно")
                points += 1
            else:
                print("Неправильно")
        print(f"Всего очков: {points}")


# А теперь пример работы:
game = Quiz([Question("2+2=4?", "Да", "Нет", "52", "Что?", 1),
             Question("Арифметический корень из -5 - это...?", "Да", "Конечно Криштиану Роналду", "Невозможно", "0", 3)])
game.start_game()
