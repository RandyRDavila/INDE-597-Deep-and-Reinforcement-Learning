import enum
import numpy as np

class Player(enum.Enum):
    """
    A player is an enum class that contains the values of the players in the game.
    """
    A = 1.0
    B = -1.0
    none = 0.0

class Agent:
    """
    An agent is a player (class) with a policy (callable). The policy is a function
    that takes a board and returns a move. The agent is a callable that takes a board
    and returns a move.

    Args:
    player: Player
    policy: callable

    Methods:
    __call__(self, board: np.ndarray) -> tuple
    __repr__(self) -> Player

    Example:
    ```python
    >>> from policies import random_policy
    >>> from board_classes import Agent, Player
    >>> agentA = Agent(Player.A, random_policy)
    >>> move = agentA(board)
    ```
    """
    def __init__(self, player: Player, policy: callable):
        self.player = player
        self.policy = policy

    def __call__(self, board: np.ndarray) -> tuple:
        return self.policy(board, self.player)

    def __repr__(self) -> Player:
        return self.player

class GameBoard:
    """
    A game board is a class that contains the logic of a game. The logic is a dictionary
    of functions that define the game. The game board is a callable that takes a player
    and a move and returns the new board.

    Args:
    logic: dict[str, callable]

    Methods:
    reset(self) -> tuple
    render(self) -> None
    winner(self) -> Player
    valid_moves(self, player=None) -> list[tuple[int, int]]
    draw(self) -> bool
    game_over(self) -> bool
    play(self, player, move, mutate=True) -> np.ndarray
    __call__(self, player, move) -> np.ndarray
    __repr__(self) -> str

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_logic
    >>> board = GameBoard(tictactoe_logic)
    >>> board.reset()
    >>> board.render()
    >>> board.winner()
    >>> board.valid_moves()
    >>> board.draw()
    >>> board.game_over()
    >>> board.play(Player.A, (0, 0))
    >>> board(Player.B, (1, 1))
    >>> board
    ```
    """
    def __init__(self, logic: dict[str, callable]):
        self.logic = logic

    ########################### Logic Methods ###########################
    def reset(self) -> tuple:
        self.board = self.logic["board"].copy()
        return self.board, False

    def render(self) -> None:
        return self.logic["render"](self.board)

    def winner(self) -> Player:
        return self.logic["winner"](self.board)

    def valid_moves(self, player=None) -> list[tuple[int, int]]:
        return self.logic["valid_moves"](self.board, player=player)

    def play(self, player, move, mutate=True) -> np.ndarray:
        return self.logic["play"](self.board, player, move, mutate=mutate)

    ########################### Derived Game Methods ###########################

    def draw(self) -> bool:
        return len(self.valid_moves()) == 0 and self.winner() == Player.none

    def game_over(self) -> bool:
        return self.winner() != Player.none or self.draw()

    ############################# Magic Methods ###########################

    def __call__(self, player, move) -> np.ndarray:
        return self.play(player, move, mutate=True)

    def __repr__(self) -> str:
        return self.board.__repr__()
