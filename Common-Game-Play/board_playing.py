from board_classes import Player, Agent
from policies import random_policy
import numpy as np

def play_random_game(board:np.ndarray, render=False) -> None:
    """
    Play a random game on the board.

    Args:
    board: np.ndarray
    render: bool

    Returns:
    None
    """
    # Reset the board to begin the game.
    board.reset()

    # Render the board if requested.
    if render:
        board.render()

    # Define the two agents.
    agentA = Agent(Player.A, random_policy)
    agentB = Agent(Player.B, random_policy)

    # Play the game.
    while True:
        # Agent A plays first.
        move = agentA(board)

        # Agent A plays the move.
        board(agentA.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            return None

        # Agent B plays second.
        move = agentB(board)

        # Agent B plays the move.
        board(agentB.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            return None
