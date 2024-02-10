import matplotlib.pyplot as plt
import numpy as np

def generate_episode(env, policy=None):
    episode = []
    state = env.reset()
    action = policy[state] if policy else env.action_space.sample()

    while True:
        next_state, reward, done  = env.step(action)
        episode.append((state, action, reward))
        if done:
            break
        state = next_state
        action = policy[state] if policy else env.action_space.sample()
    return episode

def generate_episodes(env, policy, num_episodes):
    episodes = []
    for _ in range(num_episodes):
        episodes.append(generate_episode(env, policy))
    return episodes

def win_percentage(env, policy, num_episodes):
    wins = 0
    for _ in range(num_episodes):
        episode = generate_episode(env, policy)
        if episode[-1][-1] == 1:
            wins += 1
    return wins / num_episodes * 100

def prepare_data_for_plot(V, usable_ace):
    player_sums = sorted(set(key[0] for key in V.keys() if 12 <= key[0] <= 21 and key[2] == usable_ace))
    dealer_showing = sorted(set(key[1] for key in V.keys() if key[2] == usable_ace))
    Y, X = np.meshgrid(player_sums, dealer_showing)
    Z = np.zeros_like(X, dtype=float)

    # Outer loop for dealer's card.
    for i, dealer_card in enumerate(dealer_showing):
        # Inner loop for player's sum.
        for j, player_sum in enumerate(player_sums):
            # Assign values accordingly.
            Z[i, j] = V.get((player_sum, dealer_card, usable_ace), np.nan)

    return X, Y, Z

def plot_value_function(V, usable_ace, title):
    X, Y, Z = prepare_data_for_plot(V, usable_ace)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Dealer\'s Showing Card')
    ax.set_ylabel('Player\'s Current Sum')
    ax.set_zlabel('Value')
    ax.set_title(title)
    fig.colorbar(surf)
    plt.show()

def plot_value_function_subplot(V_first, V_second, title_first, title_second):
    fig = plt.figure(figsize=(20, 14))

    for i, usable_ace in enumerate([0, 1]):
        X, Y, Z_first = prepare_data_for_plot(V_first, usable_ace)
        ax = fig.add_subplot(2, 2, i + 1, projection='3d')
        surf = ax.plot_surface(X, Y, Z_first, cmap='viridis', edgecolor='none')
        ax.set_xlabel("Dealer's Showing Card")
        ax.set_ylabel("Player's Current Sum")
        ax.set_zlabel('Value')
        ax.set_title(f"{title_first} - Usable Ace: {bool(usable_ace)}")
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

        X, Y, Z_second = prepare_data_for_plot(V_second, usable_ace)
        ax = fig.add_subplot(2, 2, i + 3, projection='3d')
        surf = ax.plot_surface(X, Y, Z_second, cmap='viridis', edgecolor='none')
        ax.set_xlabel("Dealer's Showing Card")
        ax.set_ylabel("Player's Current Sum")
        ax.set_zlabel('Value')
        ax.set_title(f"{title_second} - Usable Ace: {bool(usable_ace)}")
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()
