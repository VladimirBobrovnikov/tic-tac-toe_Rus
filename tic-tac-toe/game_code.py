import random  # Used for easy bot


def field_output():
    print(*('X\\Y', 1, 2, 3))
    i = 1
    for line_game in moves:
        print(f' {i} ', end=' ')
        print('|'.join(line_game))
        i += 1


def checking_the_victory():
    for i in range(3):
        if moves[i][0] != '-':
            if moves[i][0] == moves[i][1] == moves[i][2]:
                print(f"Результат игры:\n{sign_player[moves[i][0]]}")
                return 1
            elif i == 0 and moves[0][i] == moves[1][i] == moves[2][i]:
                print(f"Результат игры:\n{sign_player[moves[0][i]]}")
                return 1
            elif i == 0 and moves[0][0] == moves[1][1] == moves[2][2]:
                print(f"Результат игры:\n{sign_player[moves[0][0]]}")
                return 1
        if moves[0][i] != '-':
            if moves[0][i] == moves[1][i] == moves[2][i]:
                print(f"Результат игры:\n{sign_player[moves[0][i]]}")
                return 1
        if i == 2 and moves[0][2] != '-' and moves[0][2] == moves[1][1] == moves[2][0]:
            print(f"Результат игры:\n{sign_player[moves[0][2]]}")
            return 1
    if number_step == 9:
        print(f"Результат игры:\n{sign_player['n']}")
        return 1
    return 0


def player_step():
    while True:
        text_step = f'Ходит игрок {number_player}:\nЧтобы сделать ход введите координаты клетки "X" "Y"\n'
        field_output()
        try:
            step_player = list(map(int, input(text_step).split()))
            if len(step_player) != 2:
                print('Некорректный ввод данных')
                continue
        except ValueError:
            print('Некорректный ввод данных')
            continue
        try:
            if moves[step_player[0] - 1][step_player[1] - 1] != '-':
                print('Клетка занята')
                continue
        except IndexError:
            print('Некорректный ввод данных')
            continue
        moves[step_player[0] - 1][step_player[1] - 1] = 'x' if number_player == 1 else '0'
        break


def step_easy_bot():
    field_output()
    for i in range(3):
        if ''.join(moves[i]).replace('-', '') == 'xx':
            # checking lines for the likelihood of losing
            for j in range(3):
                if moves[i][j] == '-':
                    x = i
                    y = j
                    return x, y
        if (moves[0][i] + moves[1][i] + moves[2][i]).replace('-', '') == 'xx':
            # checking columns for the likelihood of losing
            for j in range(3):
                if moves[j][i] == '-':
                    x = j
                    y = i
                    return x, y
    if (moves[0][2] + moves[1][1] + moves[2][0]).replace('-', '') == 'xx':
        # checking the diagonals for the possibility of losing
        if moves[0][2] == '-':
            x, y = 0, 2
            return x, y
        elif moves[2][0] == '-':
            x, y = 2, 0
            return x, y
        else:
            x, y = 1, 1
            return x, y
    if (moves[0][0] + moves[1][1] + moves[2][2]).replace('-', '') == 'xx':
        # checking the diagonals for the possibility of losing
        for j in range(3):
            if moves[j][j] == '-':
                x = j
                y = j
                return x, y
    while True:
        x = random.randrange(0, 2, 1)
        y = random.randrange(0, 2, 1)
        if moves[x][y] == '-':
            return x, y


def step_hard_bot():  #invincible bot
    field_output()
    if number_step == 1:  #First check the middle cage
        if moves[1][1] == 'x':
            x = random.randrange(0, 2, 2)
            y = random.randrange(0, 2, 2)
            return x, y
        else:
            x = y = 1
            return x, y
    else:
        if (moves[0][0] + moves[1][1] + moves[2][2]).replace('-', '') == '00':
            #checking the diagonals for the possibility of winning
            for j in range(3):
                if moves[j][j] == '-':
                    x = j
                    y = j
                    return x, y
        if (moves[0][2] + moves[1][1] + moves[2][0]).replace('-', '') == '00':
            #checking the diagonals for the possibility of winning
            if moves[0][2] == '-':
                x, y = 0, 2
                return x, y
            elif moves[2][0] == '-':
                x, y = 2, 0
                return x, y
            else:
                x, y = 1, 1
                return x, y
        for i in range(3):
            if ''.join(moves[i]).replace('-', '') == '00':
                #checking the lines for the possibility of winning
                for j in range(3):
                    if moves[i][j] == '-':
                        x = i
                        y = j
                        return x, y
            if (moves[0][i] + moves[1][i] + moves[2][i]).replace('-', '') == '00':
                #checking columns for the possibility of winning
                for j in range(3):
                    if moves[j][i] == '-':
                        x = j
                        y = i
                        return x, y
            if ''.join(moves[i]).replace('-', '') == 'xx':
                #checking lines for the likelihood of losing
                for j in range(3):
                    if moves[i][j] == '-':
                        x = i
                        y = j
                        return x, y
            if (moves[0][i] + moves[1][i] + moves[2][i]).replace('-', '') == 'xx':
                #checking columns for the likelihood of losing
                for j in range(3):
                    if moves[j][i] == '-':
                        x = j
                        y = i
                        return x, y
        if (moves[0][2] + moves[1][1] + moves[2][0]).replace('-', '') == 'xx':
            #checking the diagonals for the possibility of losing
            if moves[0][2] == '-':
                x, y = 0, 2
                return x, y
            elif moves[2][0] == '-':
                x, y = 2, 0
                return x, y
            else:
                x, y = 1, 1
                return x, y
        if (moves[0][0] + moves[1][1] + moves[2][2]).replace('-', '') == 'xx':
            #checking the diagonals for the possibility of losing
            for j in range(3):
                if moves[j][j] == '-':
                    x = j
                    y = j
                    return x, y
        if moves[0][0] == '-':  #empty corners check
            x, y = 0, 0
        elif moves[0][2] == '-':
            x, y = 0, 2
        elif moves[2][0] == '-':
            x, y = 2, 0
        elif moves[2][2] == '-':
            x, y = 2, 2
        elif moves[0][1] == '-':  #search for a possible move
            x, y = 0, 1
        elif moves[1][0] == '-':
            x, y = 1, 0
        elif moves[1][2] == '-':
            x, y = 1, 2
        elif moves[2][0] == '-':
            x, y = 2, 0
        return x, y


moves = [  #playing field
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
number_step = 0
number_player = 1


while True:
    player_or_bot = input('Вы желаете сыграть против компьютера?\n(y/n)\n')
    if player_or_bot == 'y' or player_or_bot == 'n':
        break
    else:
        print('Некорректный ввод данных')

if player_or_bot == 'y':
    while True:
        easy_or_hard = input('Уровень сложности: Easy?\n(y/n)\n')
        if easy_or_hard == 'y' or easy_or_hard == 'n':
            break
        else:
            print('Некорректный ввод данных')
    sign_player = {'0': 'Победил Компьютер', 'x': 'победил Игрок 1', 'n': 'Ничья'}
    #Dictionary for the conclusion who won
else:
    sign_player = {'x': 'Победил Игрок 1', '0': 'победил Игрок 2', 'n': 'Ничья'}
    #Dictionary for the conclusion who won

while True:
    player_step()
    number_step += 1
    if number_step > 4 and checking_the_victory() == 1:
        field_output()
        break
    if player_or_bot == 'n':
        number_player = 2 if number_player == 1 else 1
    else:
        if easy_or_hard == 'y':
            x, y = step_easy_bot()
        else:
            x, y = step_hard_bot()
        moves[x][y] = '0'
        number_step += 1
    if number_step > 4 and checking_the_victory() == 1:
        field_output()
        break
