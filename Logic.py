from random import random
from copy import deepcopy


def test_print(mas):
    print('-' * 11)
    for i in mas:
        print('|', *i, '|')
    print('-' * 11)


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                empty.append(get_num_f_ind(i, j))
    return empty


def get_num_f_ind(i, j):
    return i * 4 + j + 1


def get_ind_f_num(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert2or4(mas, x, y):
    if random() <= 0.6:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def is_zero_in_mas(mas):
    for i in mas:
        if 0 in i:
            return True
    return False


def can_move(mas):
    for i in range(len(mas) - 1):
        for j in range(len(mas[i])):
            if mas[i][j] == mas[i + 1][j] or mas[j][i] == mas[j][i + 1]:
                return True
    return False


# --------------------MOVE_BLOCKS--------------------
def move_left(mas):
    old_mas = deepcopy(mas)
    delta = 0
    for row in mas:
        lenrow = len(row)
        rangLen_1 = range(lenrow - 1)

        # move left
        for col in rangLen_1:
            if (row[col] == 0):
                icol = col + 1
                while icol < lenrow:
                    if (row[icol] != 0):
                        row[col] = row[icol]
                        row[icol] = 0
                        break
                    icol += 1

        # concat
        for col in rangLen_1:
            if row[col] == row[col + 1]:
                row[col] *= 2
                delta += row[col]
                row[col + 1] = 0

        # move left again
        for col in rangLen_1:
            if (row[col] == 0):
                icol = col + 1
                while icol < lenrow:
                    if (row[icol] != 0):
                        row[col] = row[icol]
                        row[icol] = 0
                        break
                    icol += 1
    return mas, delta, not old_mas == mas


def move_right(mas):
    old_mas = deepcopy(mas)
    delta = 0
    for row in mas:
        lenrow = len(row)
        brpoint = range(lenrow - 1, 0, -1)

        # move right
        for col in brpoint:
            if (row[col] == 0):
                icol = col - 1
                while icol >= 0:
                    if (row[icol] != 0):
                        row[col] = row[icol]
                        row[icol] = 0
                        break
                    icol -= 1

        # concat
        for col in brpoint:
            if row[col] == row[col - 1]:
                row[col] *= 2
                delta += row[col]
                row[col - 1] = 0

        # move right again
        for col in brpoint:
            if (row[col] == 0):
                icol = col - 1
                while icol >= 0:
                    if (row[icol] != 0):
                        row[col] = row[icol]
                        row[icol] = 0
                        break
                    icol -= 1
    return mas, delta, not old_mas == mas


def move_down(mas):
    old_mas = deepcopy(mas)
    delta = 0
    for col in range(len(mas)):
        lencol = len(mas[col])
        brpoint = range(lencol - 1, 0, -1)

        # move down
        for row in brpoint:
            if (mas[row][col] == 0):
                irow = row - 1
                while irow >= 0:
                    if (mas[irow][col] != 0):
                        mas[row][col] = mas[irow][col]
                        mas[irow][col] = 0
                        break
                    irow -= 1

        # concat
        for row in brpoint:
            if mas[row][col] == mas[row - 1][col]:
                mas[row][col] *= 2
                delta += mas[row][col]
                mas[row - 1][col] = 0

        # move down again
        for row in brpoint:
            if (mas[row][col] == 0):
                irow = row - 1
                while irow >= 0:
                    if (mas[irow][col] != 0):
                        mas[row][col] = mas[irow][col]
                        mas[irow][col] = 0
                        break
                    irow -= 1
    return mas, delta, not old_mas == mas


def move_up(mas):
    old_mas = deepcopy(mas)
    delta = 0
    for col in range(len(mas)):
        lencol = len(mas[col])  # row == col, don`t worry
        rangLen_1 = range(lencol - 1)

        # move up
        for row in rangLen_1:
            if (mas[row][col] == 0):
                irow = row + 1
                while irow < lencol:
                    if (mas[irow][col] != 0):
                        mas[row][col] = mas[irow][col]
                        mas[irow][col] = 0
                        break
                    irow += 1

        # concat
        for row in rangLen_1:
            if mas[row][col] == mas[row + 1][col]:
                mas[row][col] *= 2
                delta += mas[row][col]
                mas[row + 1][col] = 0

        # move up again
        for row in rangLen_1:
            if (mas[row][col] == 0):
                irow = row + 1
                while irow < lencol:
                    if (mas[irow][col] != 0):
                        mas[row][col] = mas[irow][col]
                        mas[irow][col] = 0
                        break
                    irow += 1
    return mas, delta, not old_mas == mas

# --------------------MOVE_BLOCKS--------------------
