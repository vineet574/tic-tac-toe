import random
import json
import os

SCORE_FILE = "scores.json"
UNDO_LIMIT = 3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)): return True
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
            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter two numbers separated by space.")

def get_computer_move(board, computer_player, human_player, difficulty="hard"):
    if difficulty == "easy":
        return random.choice(get_available_moves(board))
    for row, col in get_available_moves(board):
        board[row][col] = computer_player
        if check_winner(board, computer_player):
            board[row][col] = " "
            return row, col
        board[row][col] = " "
    for row, col in get_available_moves(board):
        board[row][col] = human_player
        if check_winner(board, human_player):
            board[row][col] = " "
            return row, col
        board[row][col] = " "
    if board[1][1] == " ":
        return 1, 1
    return random.choice(get_available_moves(board))

def undo_move(board, moves_stack, steps=1):
    for _ in range(min(steps, len(moves_stack))):
        row, col = moves_stack.pop()
        board[row][col] = " "

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {"X": 0, "O": 0}

def replay_game(moves):
    board = [[" "]*3 for _ in range(3)]
    print("\nReplaying the game:")
    for i, (r, c, p) in enumerate(moves):
        board[r][c] = p
        print(f"\nMove {i+1}: Player {p}")
        print_board(board)

def tic_tac_toe():
    scores = load_scores()
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        moves_stack = []
        history = []

        player_choice = input("Do you want to play as X or O? ").upper()
        while player_choice not in ["X", "O"]:
            player_choice = input("Invalid choice. Please enter X or O: ").upper()

        human_player = player_choice
        computer_player = "O" if human_player == "X" else "X"

        play_against_computer = input("Play against the computer? (yes/no): ").lower() == "yes"
        difficulty = "hard" if play_against_computer and input("Choose difficulty (easy/hard): ").lower() == "hard" else "easy"

        turn = 0
        while True:
            print_board(board)
            current_player = players[turn % 2]
            if not play_against_computer or current_player == human_player:
                row, col = get_player_move(board)
            else:
                row, col = get_computer_move(board, computer_player, human_player, difficulty)
                print(f"Computer plays at row {row}, column {col}")

            board[row][col] = current_player
            moves_stack.append((row, col))
            history.append((row, col, current_player))

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                scores[current_player] += 1
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            turn += 1

            if len(moves_stack) >= 1:
                undo = input("Undo moves? Enter number (0 to skip): ")
                if undo.isdigit():
                    undo_n = int(undo)
                    if 1 <= undo_n <= UNDO_LIMIT:
                        undo_move(board, moves_stack, undo_n)
                        history = history[:-undo_n]
                        turn -= undo_n

        print(f"Scores: X - {scores['X']}, O - {scores['O']}")
        save_scores(scores)

        if input("Replay this game? (yes/no): ").lower() == "yes":
            replay_game(history)

        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

tic_tac_toe()
