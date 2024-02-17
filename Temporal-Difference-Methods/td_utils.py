from tictactoe_class import TicTacToe
import numpy as np

def state_to_string(state):
    return ''.join(str(cell) for row in state for cell in row)

def random_move(state):
    possible_actions = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0]
    return possible_actions[np.random.randint(len(possible_actions))] if possible_actions else None

def simulate_game(trained_agent, display=True):
    env = TicTacToe()  # Reset the environment for a new game
    game_over = False
    while not game_over:
        # Q-learning agent's turn (Player 1)
        current_state = state_to_string(env.board)
        possible_actions = [(i, j) for i in range(3) for j in range(3) if env.board[i][j] == 0]
        action = trained_agent.choose_action(current_state, possible_actions)
        env.make_move(*action)
        if display:
            print(f"Agent's move (Player 1):")
            env.render()
        game_over, reward = env.is_game_over()

        if game_over:
            if reward == 1:
                print("Trained agent wins!")
            elif reward == -1:
                print("Random agent wins!")
            else:
                print("It's a draw!")
            break

        # Random agent's turn (Player 2)
        action = random_move(env.board)
        if action:
            env.make_move(*action)
            if display:
                print(f"Random agent's move (Player 2):")
                env.render()
            game_over, reward = env.is_game_over()

            if game_over:
                if reward == 1:
                    print("Trained agent wins!")
                elif reward == -1:
                    print("Random agent wins!")
                else:
                    print("It's a draw!")
                break