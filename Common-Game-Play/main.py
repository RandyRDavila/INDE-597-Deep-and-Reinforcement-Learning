from tictactoe_logic import tictactoe_logic
from board_classes import GameBoard, Player
from board_playing import play_game

board = GameBoard(tictactoe_logic)

play_game(board, render=True)

