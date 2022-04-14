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


def check_victory(board):
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
        return board[0][2]
    else:
        return 0


def check_draw(board):
    draw = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                draw = False
    return draw


def check_game_result(board):
    winner = check_victory(board)
    if winner != 0:
        print("player " + str(winner) + " won")
        return True
    elif check_draw(board):
        print("its a draw")
        return True


def validate_player_input(player_input: int):
    return bool(0 <= player_input <= 2)


def get_player_input(player, row_or_col):
    while True:
        player_input = input("player " + str(player) + " please enter " + row_or_col + " #:")
        if player_input.isdigit():
            player_input = int(player_input)
            if validate_player_input(player_input):
                return player_input
            else:
                print("input invalid - try again")


def place_token(board, player):
    while True:
        row = get_player_input(player, "row")
        col = get_player_input(player, "col")
        if spot_is_empty(board, row, col):
            board[row][col] = player
            return True
        else:
            print("spot not empty - try again")


def spot_is_empty(board, row, col):
    return board[row][col] == 0


def start_new_game():
    print("Welcome to TicTacToe.")
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    players_turn(board)


def ask_for_next_round():
    while True:
        player_input = input("Game Over - Do you want to play another round? [y/n]")
        if player_input == "y":
            return True
        elif player_input == "n":
            return False
        else:
            print("Input invalid.")


def players_turn(board):
    print_board(board)
    while True:
        for i in range(1, 3):
            place_token(board, i)
            print_board(board)
            if check_game_result(board):
                if ask_for_next_round():
                    start_new_game()
                else:
                    print("Thanks for the ride- see you soon")
                    exit()


if __name__ == "__main__":
    start_new_game()
