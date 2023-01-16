toe_field = [[" "] * 3 for i in range(3)]


def greeting():
    print("--------------------------------------")
    print("Приветствуем в игре 'Крестики-нолики!'")
    print("          Формат ввода: x y           ")
    print("          x - номер строки            ")
    print("          у - номер столбца           ")
    print("--------------------------------------")


def toe_board():
    print(f"|   | 0 | 1 | 2 |")
    print(f"_________________")
    for i in range(3):
        # первый вариант print(f"| {i} | {toe_field[i][0]} | {toe_field[i][1]} | {toe_field[i][2]} |")
        row = " | ".join(toe_field[i])
        print(f"| {i} | {row} |")
        print(f"_________________")


# toe_board()


def position_request():
    while True:
        coordinates = input("Ваш ход! Введите две координаты: ").split()

        if len(coordinates) != 2:
            print("Ошибка! Вы ввели неправильное количество координат")
            continue

        x, y = coordinates

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Ошибка! Введите координаты в диапазоне от 0 до 2:")
            continue

        if toe_field[x][y] != " ":
            print("Клетка уже занята")
            continue

        return x, y


# print(position_request())


def check_win():
    victory_cond = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for line in victory_cond:
        symbols = []

        for coord in line:
            symbols.append(toe_field[coord[0]][coord[1]])

        if symbols == ["X", "X", "X"]:
            print("Конец игры: Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Конец игры: Выиграл 0!")
            return True
    return False


def main():
    greeting()
    for move in range(1, 10):

        toe_board()

        if move % 2 == 1:
            print("Ходит крестик")
        else:
            print("Ходит нолик")

        x, y = position_request()

        if move % 2 == 1:
            toe_field[x][y] = "X"
        else:
            toe_field[x][y] = "0"

        if check_win():
            break

        if move == 9:
            print("Конец игры: Ничья!")
            break


main()
