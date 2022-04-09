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


def check_result():
    return False


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




while True:
    print_board(gaming_board)
    placing(1)
    print_board(gaming_board)
    placing(2)

    exit()
