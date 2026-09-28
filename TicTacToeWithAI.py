import random

board = [[" " for _ in range(3)] for _ in range(3)]


def print_board():
    print("\n")
    for r in range(3):
        print(f" {board[r][0]} | {board[r][1]} | {board[r][2]} ")
        if r < 2:
            print("---+---+---")
    print("\n")


def get_empty_positions():
    empty = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                empty.append((r, c))
    return empty


def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def find_winning_or_blocking_move(symbol):
    for r, c in get_empty_positions():
        board[r][c] = symbol
        if check_winner(symbol):
            board[r][c] = " "
            return (r, c)
        board[r][c] = " "
    return None


def bot_move(bot_symbol, human_symbol):
    empty = get_empty_positions()
    if not empty:
        return

    win_move = find_winning_or_blocking_move(bot_symbol)
    if win_move:
        board[win_move[0]][win_move[1]] = bot_symbol
        return

    block_move = find_winning_or_blocking_move(human_symbol)
    if block_move:
        board[block_move[0]][block_move[1]] = bot_symbol
        return

    if board[1][1] == " ":
        board[1][1] = bot_symbol
        return

    r, c = random.choice(empty)
    board[r][c] = bot_symbol


def main():
    human = "X"
    bot = "O"
    current_player = human

    print("=== Tic-Tac-Toe ===")
    print_board()

    while True:
        if not get_empty_positions():
            print("The game is a draw!")
            break

        if current_player == human:
            valid_move = False
            while not valid_move:
                try:
                    row_input = int(input("Enter row (1-3): ")) - 1
                    col_input = int(input("Enter col (1-3): ")) - 1

                    if row_input in range(3) and col_input in range(3):
                        if board[row_input][col_input] == " ":
                            board[row_input][col_input] = human
                            valid_move = True
                        else:
                            print("That cell is already taken! Try again.")
                    else:
                        print("Values must be between 1 and 3.")
                except ValueError:
                    print("Invalid input. Please enter numbers 1, 2, or 3.")

            print_board()

            if check_winner(human):
                print("You won the game!")
                break

            current_player = bot

        else:
            print("Bot's turn ('O'):")
            bot_move(bot, human)
            print_board()

            if check_winner(bot):
                print("Bot won the game!")
                break

            current_player = human


if __name__ == "__main__":
    main()