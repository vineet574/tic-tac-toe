import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def is_board_full(board):
    return not any(" " in row for row in board)

def get_player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Row and column must be between 0-2, and the cell must be empty.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def get_computer_move(board, computer_player, human_player):
    # 1. Check if computer can win in the next move
    for row, col in get_available_moves(board):
        board[row][col] = computer_player
        if check_winner(board, computer_player):
            board[row][col] = " "  # Undo the move for now
            return row, col
        board[row][col] = " "  # Undo the move

    # 2. Check if the player can win in the next move and block them
    for row, col in get_available_moves(board):
        board[row][col] = human_player
        if check_winner(board, human_player):
            board[row][col] = " "  # Undo the move for now
            return row, col
        board[row][col] = " "  # Undo the move

    # 3. Choose the center if it's free
    if board[1][1] == " ":
        return 1, 1

    # 4. Choose a random available move
    return random.choice(get_available_moves(board))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_choice = input("Do you want to play as X or O? ").upper()

    while player_choice not in ["X", "O"]:
        player_choice = input("Invalid choice. Please enter X or O: ").upper()

    if player_choice == "X":
        human_player = "X"
        computer_player = "O"
    else:
        human_player = "O"
        computer_player = "X"

    turn = 0
    play_against_computer = input("Do you want to play against the computer? (yes/no): ").lower() == "yes"

    while True:
        print_board(board)

        if turn % 2 == 0:
            if not play_against_computer or human_player == players[turn % 2]:
                row, col = get_player_move(board)
            else:
                row, col = get_computer_move(board, computer_player, human_player)
                print(f"Computer plays at row {row}, column {col}")
        else:
            if not play_against_computer or human_player == players[turn % 2]:
                row, col = get_player_move(board)
            else:
                row, col = get_computer_move(board, computer_player, human_player)
                print(f"Computer plays at row {row}, column {col}")

        board[row][col] = players[turn % 2]

        if check_winner(board, players[turn % 2]):
            print_board(board)
            print(f"Player {players[turn % 2]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

tic_tac_toe()
