from tictactoe_logic import tictactoe_logic
from board_classes import GameBoard, Player
from board_playing import play_random_game


# Create the game board.
board = GameBoard(tictactoe_logic)

# Play a random game.
play_random_game(board, render=True)
