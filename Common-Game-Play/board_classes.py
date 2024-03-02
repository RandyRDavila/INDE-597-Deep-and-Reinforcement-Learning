import enum
import numpy as np

class Player(enum.Enum):
    A = 1.0
    B = -1.0
    none = 0.0

class Agent:
    def __init__(self, player, policy):
        self.player = player
        self.policy = policy

    def __call__(self, board):
        return self.policy(board, self.player)

    def __repr__(self):
        return self.name


class GameBoard:
    def __init__(self, logic):
        self.logic = logic

    def reset(self):
        self.board = self.logic["board"].copy()
        return self.board, False

    def render(self):
        return self.logic["render"](self.board)

    def winner(self):
        return self.logic["winner"](self.board)

    def draw(self):
        return self.logic["draw"](self.board)

    def game_over(self):
        return self.logic["game_over"](self.board)

    def valid_moves(self, player=None):
        return self.logic["valid_moves"](self.board, player=player)

    def play(self, player, move, mutate=True):
        return self.logic["play"](self.board, player, move, mutate=mutate)

    def __call__(self, player, move):
        return self.play(player, move, mutate=True)

    def __repr__(self):
        return self.board.__repr__()

