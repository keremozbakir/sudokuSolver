board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 0, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 0]
]


def show_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-----------------------------------------')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', "  ", end="")
            print(bo[i][j], "  ", end="")
            if j == 8:
                print('\n')


## bosluk bulma

def bos_bul(bo):
    for y in range(9):
        for x in range(9):
            if bo[y][x] == 0:
                return y, x

    return None


def valid(bo, num, pos):
    for i in range(9):
        # yatay olarak kontrol
        # print('burada')
        # print(pos[0])
        if bo[pos[0]][i] == num:
            return False
        # dikey kontrol
        if bo[i][pos[1]] == num:
            return False

        # kareleri kontrol

        kare_x = pos[1] // 3

        kare_y = pos[0] // 3
        for k in range(kare_y * 3, kare_y * 3 + 3):
            for r in range(kare_x * 3, kare_x * 3 + 3):

                if bo[k][r] == num and (k, r) != pos:
                    return False

    # print(bo)
    return True


def dogru_sayi(bo, numara, pos):
    for i in range(9):
        if bo[pos[0]][i] == numara:
            return False

        if bo[i][pos[1]] == numara:
            return False

        kare_x = pos[1] // 3

        kare_y = pos[0] // 3
        for k in range(kare_y * 3, kare_y * 3 + 3):
            for r in range(kare_x * 3, kare_x * 3 + 3):

                if bo[k][r] == numara and (k, r) != pos:
                    return False

    return True


def solve(bo):
    bos_var = bos_bul(bo)

    if not bos_var:
        # print(bo)
        return True

    else:
        row, col = bos_var

    for i in range(1, 10):
        if dogru_sayi(bo, i, (row, col)):  # is True

            bo[row][col] = i
            # print(colored(bo,'red'))
            # print('######################################################')
            # print(bo)
            if solve(bo):
                # print(bo)
                return True

            bo[row][col] = 0

    return False


solve(board)

show_board(board)
