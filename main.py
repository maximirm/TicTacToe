gaming_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

LF = {1: "X", 2: "O", 0: " "}


def print_board(board):
    print("    0   1   2")
    print("   -----------")
    print(f"0 | {LF[board[0][0]]} | {LF[board[0][1]]} | {LF[board[0][2]]} |")
    print("   -----------")
    print(f"1 | {LF[board[1][0]]} | {LF[board[1][1]]} | {LF[board[1][2]]} |")
    print("   -----------")
    print(f"2 | {LF[board[2][0]]} | {LF[board[2][1]]} | {LF[board[2][2]]} |")
    print("   -----------")


def check_board(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][1]
    else:
        return 0


def check_draw(board):
    draw = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                draw = False
    return draw


def check_result(board):
    winner = check_board(board)
    if winner != 0:
        print("player " + str(winner) + " won")
        exit()
    elif check_draw(board):
        print("its a draw")
        exit()


def validate_input(player_input: int):
    return bool(0 <= player_input <= 2)


def get_player_input(player, row_or_col):
    while True:
        player_input = input("player " + str(player) + " please enter " + row_or_col + " #:")
        if player_input.isdigit():
            player_input = int(player_input)
            if validate_input(player_input):
                return player_input


def placing(player):
    while True:
        row = get_player_input(player, "row")
        col = get_player_input(player, "col")
        if gaming_board[row][col] == 0:
            gaming_board[row][col] = player
            return True
        else:
            print("spot not empty")


print_board(gaming_board)
while True:
    placing(1)
    print_board(gaming_board)
    check_result(gaming_board)
    placing(2)
    print_board(gaming_board)
    check_result(gaming_board)


