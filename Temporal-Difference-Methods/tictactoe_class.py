import numpy as np
from tabulate import tabulate


class TicTacToe:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1  # Player 1 starts

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != 0 for i in range(3) for j in range(3))

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = 1 if self.current_player == 2 else 2
            return True
        return False

    def display_board(self):
        symbols = {0: ' ', 1: 'X', 2: 'O'}
        for row in self.board:
            print('|'.join(symbols[cell] for cell in row))
            print("-"*5)

    def is_game_over(self):
        if self.check_win(1):
            return True, 1
        elif self.check_win(2):
            return True, -1
        elif self.is_draw():
            return True, 0
        return False, 0

    def render(self):
        board = np.zeros((3, 3), dtype=str)
        for ii in range(3):
            for jj in range(3):
                if self.board[ii][jj] == 0:
                    board[ii, jj] = "-"
                elif self.board[ii][jj] == 1:
                    board[ii, jj] = "X"
                elif self.board[ii][jj] == 2:
                    board[ii, jj] = "O"
        board = tabulate(board, tablefmt="fancy_grid")
        print(board)
