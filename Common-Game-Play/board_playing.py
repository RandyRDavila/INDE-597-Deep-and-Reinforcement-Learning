import random
from board_classes import Player

class Agent:
    def __init__(self, player, policy):
        self.player = player
        self.policy = policy

    def __call__(self, board):
        return self.policy(board, self.player)

def random_policy(board, player):
    valid_moves = board.valid_moves(player)
    return random.choice(valid_moves)


def play_game(board, render=False):
    _, done = board.reset()

    while True:
        valid_moves = board.valid_moves(player=Player.A)
        move = random.choice(valid_moves)
        board(Player.A, move)
        if render:
            board.render()
        if board.game_over():
            break
        valid_moves = board.valid_moves(player=Player.B)
        move = random.choice(valid_moves)
        board(Player.B, move)
        if render:
            board.render()
        if board.game_over():
            break
