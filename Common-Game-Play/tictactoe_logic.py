import numpy as np
from tabulate import tabulate
from board_classes import Player

def tictactoe_play_logic(board, player, move, mutate=True):
    x, y = move
    if not mutate:
        played_board = board.copy()
        if played_board[x, y] == Player.none.value:
            played_board[x, y] = player.value
            return played_board
        else:
            return None
    else:
        if board[x, y] == Player.none.value:
            board[x, y] = player.value
            return board
        else:
            return

def tictactoe_win(played_board, player):
    for i in range(3):
        if sum(played_board[i, :]) == 3*player.value:
            return True
        if sum(played_board[:, i]) == 3*player.value:
            return True
    if played_board[0, 0] + played_board[1, 1] + played_board[2, 2] == 3*player.value:
        return True
    if played_board[0, 2] + played_board[1, 1] + played_board[2, 0] == 3*player.value:
        return True
    return False

def tictactoe_board_valid_moves(board, player=None):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == Player.none.value]

def tictactoe_draw(board):
    player_one_win = tictactoe_win(board, Player.A)
    player_two_win = tictactoe_win(board, Player.B)
    # no_available_moves = len(valid_moves(board)) == 0
    move = tictactoe_board_valid_moves(board)
    return not (player_one_win or player_two_win) and len(move) == 0

def tictactoe_done(board):
    if tictactoe_win(board, Player.A):
        return True
    elif tictactoe_win(board, Player.B):
        return True
    elif len([(i, j) for i in range(3) for j in range(3) if board[i, j] == Player.none.value]) == 0:
        return True
    else:
        return False

def tictactoe_render(board):
    rendered_board = np.zeros((3, 3), dtype=str)
    for ii in range(3):
        for jj in range(3):
            if board[ii][jj] == Player.none.value:
                rendered_board[ii, jj] = "-"
            elif board[ii][jj] == Player.A.value:
                rendered_board[ii, jj] = "X"
            elif board[ii][jj] == Player.B.value:
                rendered_board[ii, jj] = "O"
    print(tabulate(rendered_board, tablefmt="fancy_grid"))

def tictactoe_winner(board):
    if tictactoe_win(board, Player.A):
        return Player.A
    elif tictactoe_win(board, Player.B):
        return Player.B
    else:
        return Player.none

# Each value is a function expressing the logic of TicTacToe.
tictactoe_logic = {
    "game_over" : tictactoe_done,
    "draw" : tictactoe_draw,
    "valid_moves" : tictactoe_board_valid_moves,
    "play" : tictactoe_play_logic,
    "board" : np.zeros((3, 3)),
    "render" : tictactoe_render,
    "winner" : tictactoe_winner,
}