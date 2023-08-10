field = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."], ]


def output():
    for x in field:
        print(x[0], x[1], x[2])


def dagger():
    print("Ход крестик")

    string = int(input("Введите строку: "))
    column = int(input("Введите столбец: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string - 1][column - 1] == 'x' or \
            field[string - 1][column - 1] == 'o':
        string = int(input("Введите строку заново: "))
        column = int(input("Введите столбец заново: "))

    field[string - 1][column - 1] = "x"


def zero():
    print("Ходит нолик")
    string = int(input("Введите строку: "))
    column = int(input("Введите столбец: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string - 1][column - 1] == 'x' or \
            field[string - 1][column - 1] == 'o':
        string = int(input("Введите строку заново: "))
        column = int(input("Введите столбец заново: "))

    field[string - 1][column - 1] = "o"


def check():
    for x in field:
        if x[0] == x[1] == x[2] != ".":
            print("Победил -", x[0])
            victory[0] = 1
            break
    for i in range(0, 2):
        if field[0][i] == field[1][i] == field[2][i] != ".":
            print("Победил -", field[0][i])
            victory[0] = 1
            break
    if field[0][0] == field[1][1] == field[2][2] != ".":
        print("Победил -", field[0][0])
        victory[0] = 1
    elif field[0][2] == field[1][1] == field[2][0] != ".":
        print("Победил -", field[0][2])
        victory[0] = 1


print("Крестики нолики задание 5.6.")
print("Здравствуйте, уважаемый Ментор, Вы хотите сыграть в игру?")
print("Y - Yes")
print("N - No")
answer = input()
if answer == "Y" or answer == "y":
    output()
    print("Это игровое поле")
    while True:
        k = 0
        victory = [0]

        while k < 9:
            dagger()
            k += 1
            output()
            check()
            if victory[0] == 1:
                break
            elif k == 9:
                print("Ничья")
                break
            zero()
            check()
            if victory[0] == 1:
                break
            k += 1
            output()
        print("Вы хотите продолжить?")
        print("Y - Yes")
        print("N - No")
        answer = input()
        if answer == "Y" or answer == "y":
            pass
        else:
            break

