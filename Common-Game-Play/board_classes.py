import enum
import numpy as np

class Player(enum.Enum):
    A = 1.0
    B = -1.0
    none = 0.0

class GameBoard:
    def __init__(self, logic):
        self.logic = logic

    def play(self, player, move, mutate=True):
        return self.logic["play"](self.board, player, move, mutate=mutate)

    def __call__(self, player, move):
        return self.play(player, move, mutate=True)

    def check_win_on_move(self, player, move):
        played_board = self.play(self.board, player, move, mutate=False)
        return self.logic["win_on_move"](played_board, player)

    def valid_moves(self, player=None):
        return self.logic["valid_moves"](self.board, player=player)

    def draw(self):
        return self.logic["draw"](self.board)

    def game_over(self):
        return self.logic["game_over"](self.board)

    def __repr__(self):
        return np.array2string(self.board)

    def render(self):
        return self.logic["render"](self.board)

    def reset(self):
        self.board = self.logic["board"].copy()
        return self.board, False

