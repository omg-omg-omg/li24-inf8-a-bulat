def unfilled_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '/' + ' ' * (2 * i) + '\\')
    for i in range(size - 1, -1, -1):
        print(' ' * (size - i - 1) + '\\' + ' ' * (2 * i) + '/')


def filled_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '/' + '/' * i + '\\' * i + '\\')
    for i in range(size - 1, -1, -1):
        print(' ' * (size - i - 1) + '\\' + '\\' * i + "/" * i + '/')


def diamond(size):
    unfilled_diamond(size)
    print()
    filled_diamond(size)


diamond(int(input()))
