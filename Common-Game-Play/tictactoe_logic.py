import numpy as np
from tabulate import tabulate
from board_classes import Player

def tictactoe_play_logic(board: np.ndarray, player: Player, move: tuple, mutate=True):
    """
    The logic of playing a move in TicTacToe. The function takes a board, a player, a move, and a boolean mutate.
    If mutate is False, the function returns a new board with the move played. If mutate is True, the function
    plays the move on the board and returns the board. If the move is invalid, the function returns None.

    Args:
    board: np.ndarray
    player: Player
    move: tuple[int, int]
    mutate: bool

    Returns:
    np.ndarray

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_play_logic
    >>> from board_classes import Player
    >>> import numpy as np
    >>> board = np.zeros((3, 3))
    >>> tictactoe_play_logic(board, Player.A, (0, 0))
    ```
    """
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
            return None

def tictactoe_board_valid_moves(board: np.ndarray, player=None) -> list[tuple[int, int]]:
    """
    The logic of finding the valid moves in TicTacToe. The function takes a board and a player and returns a list
    of valid moves.

    Args:
    board: np.ndarray
    player: Player

    Returns:
    list[tuple[int, int]]

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_board_valid_moves
    >>> import numpy as np
    >>> board = np.zeros((3, 3))
    >>> tictactoe_board_valid_moves(board)
    [ (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2) ]
    ```
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == Player.none.value]

def tictactoe_render(board: np.ndarray):
    """
    The logic of rendering the TicTacToe board. The function takes a board and prints the board.

    Args:
    board: np.ndarray

    Returns:
    None

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_render
    >>> import numpy as np
    >>> board = np.zeros((3, 3))
    >>> tictactoe_render(board)
    ```
    """
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

def tictactoe_winner(board: np.ndarray) -> Player:
    """
    The logic of finding the winner in TicTacToe. The function takes a board and returns the winner.

    Args:
    board: np.ndarray

    Returns:
    Player

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_winner
    >>> import numpy as np
    >>> board = np.zeros((3, 3))
    >>> tictactoe_winner(board)
    Player.none
    ```
    """
    def tictactoe_win(played_board: np.ndarray, player: Player):
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
    if tictactoe_win(board, Player.A):
        return Player.A
    elif tictactoe_win(board, Player.B):
        return Player.B
    else:
        return Player.none

# Each value is a function expressing the logic of TicTacToe.
tictactoe_logic = {
    "valid_moves" : tictactoe_board_valid_moves,
    "play" : tictactoe_play_logic,
    "board" : np.zeros((3, 3)),
    "render" : tictactoe_render,
    "winner" : tictactoe_winner,
}
