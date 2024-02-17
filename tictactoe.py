import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("300x300")
        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[tk.Button(master, text="", width=10, height=4, command=lambda row=row, col=col: self.click(row, col)) for col in range(3)] for row in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)
    
    def click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            if self.check_win(row, col):
                messagebox.showinfo("Game Over", f"{self.turn} wins!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.turn = "O" if self.turn == "X" else "X"
    
    def check_win(self, row, col):
        return (self.board[row][0] == self.board[row][1] == self.board[row][2] == self.turn or
                self.board[0][col] == self.board[1][col] == self.board[2][col] == self.turn or
                self.board[0][0] == self.board[1][1] == self.board[2][2] == self.turn or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == self.turn)
    
    def check_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))
    
    def reset(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col].config(text="")
        self.turn = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
