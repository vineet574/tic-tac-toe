import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x450")
        self.window.configure(bg="lightblue")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
        self.reset_button = tk.Button(self.window, text="Restart", font=("Arial", 14, "bold"), bg="yellow", fg="black", command=self.reset_board)
        self.reset_button.pack(pady=10)

        self.window.mainloop()

    def create_board(self):
        frame = tk.Frame(self.window, bg="lightblue")
        frame.pack()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(frame, text="", font=("Arial", 20, "bold"), width=5, height=2, bg="white",
                                               command=lambda row=r, col=c: self.on_click(row, col))
                self.buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

    def on_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg="black" if self.current_player == "X" else "red")
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
                self.disable_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.board[r][c] != "" for r in range(3) for c in range(3))

    def disable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state=tk.DISABLED)

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state=tk.NORMAL)

TicTacToe()
