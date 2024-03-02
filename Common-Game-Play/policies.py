import random

def random_policy(board, player):
    valid_moves = board.valid_moves(player=player)
    return random.choice(valid_moves)