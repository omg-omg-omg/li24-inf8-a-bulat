field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
symbol = "X"
quantity = 0


def step():
    global symbol
    global field
    print("Whats is {s}'s move? (1-9)".format(s=symbol))
    place = input()
    if len(place) == 1 and place in "123456789" and field[int(place) - 1] == " ":
        field[int(place) - 1] = symbol
        if symbol == "X":
            symbol = "O"
        elif symbol == "O":
            symbol = "X"
    else:
        step()


def draw():
    print("""{s1}|{s2}|{s3}   1 2 3
-+-+-
{s4}|{s5}|{s6}   4 5 6
-+-+-
{s7}|{s8}|{s9}   7 8 9""".format(s1=field[0], s2=field[1], s3=field[2], s4=field[3], s5=field[4], s6=field[5],
                                 s7=field[6], s8=field[7], s9=field[8]))


def check():
    if ((field[0] == "X" and field[1] == "X" and field[2] == "X") or
            (field[3] == "X" and field[4] == "X" and field[5] == "X") or
            (field[6] == "X" and field[7] == "X" and field[8] == "X") or
            (field[0] == "X" and field[3] == "X" and field[6] == "X") or
            (field[1] == "X" and field[4] == "X" and field[7] == "X") or
            (field[2] == "X" and field[5] == "X" and field[8] == "X") or
            (field[0] == "X" and field[4] == "X" and field[8] == "X") or
            (field[2] == "X" and field[4] == "X" and field[6] == "X")):
        print("X has won the game!")
        print("Thanks for playing!")
        finish_input = input()
        if finish_input or finish_input == "":
            return True
    if ((field[0] == "O" and field[1] == "O" and field[2] == "O") or
            (field[3] == "O" and field[4] == "O" and field[5] == "O") or
            (field[6] == "O" and field[7] == "O" and field[8] == "O") or
            (field[0] == "O" and field[3] == "O" and field[6] == "O") or
            (field[1] == "O" and field[4] == "O" and field[7] == "O") or
            (field[2] == "O" and field[5] == "O" and field[8] == "O") or
            (field[0] == "O" and field[4] == "O" and field[8] == "O") or
            (field[2] == "O" and field[4] == "O" and field[6] == "O")):
        print("O has won the game!")
        print("Thanks for playing!")
        finish_input = input()
        if finish_input or finish_input == "":
            return True


def quantity_check():
    global quantity
    if quantity == 9:
        print("Draw!")
        finish_input = input()
        if finish_input or finish_input == "":
            return True
    else:
        quantity += 1


def game():
    while True:
        draw()
        if check():
            break
        if quantity_check():
            break
        step()


game()
