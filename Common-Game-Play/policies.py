import random
from board_classes import Player
import numpy as np

def random_policy(board: np.ndarray, player: Player) -> tuple[int, int]:
    """
    A random policy that takes a board and a player and returns a random move.

    Args:
    board: np.ndarray
    player: Player

    Returns:
    tuple[int, int]

    Example:
    ```python
    >>> from policies import random_policy
    >>> from board_classes import Player
    >>> import numpy as np
    >>> board = np.zeros((3, 3))
    >>> random_policy(board, Player.A)
    (1, 2)
    ```
    """
    valid_moves = board.valid_moves(player=player)
    return random.choice(valid_moves)
