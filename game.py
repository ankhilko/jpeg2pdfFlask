import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.check_winner()
            self.switch_player()
        else:
            messagebox.showerror('Invalid Move', 'This cell is already occupied!')

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Проверяем выигрышные комбинации
        board.update_board()
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                self.show_winner(self.board[i][0])
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                self.show_winner(self.board[0][i])
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.show_winner(self.board[0][0])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.show_winner(self.board[0][2])

    def show_winner(self, winner):
        messagebox.showinfo('Winner', f'Player {winner} wins!')
        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]


class GameBoard:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text='', width=10, height=5,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        self.game.make_move(row, col)
        self.update_board()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.game.board[i][j])


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tic Tac Toe')

    game = TicTacToe()
    board = GameBoard(root, game)

    root.mainloop()
