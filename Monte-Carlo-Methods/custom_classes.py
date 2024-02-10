import numpy as np
from gym.envs.toy_text.blackjack import BlackjackEnv, sum_hand

class DiscreteActionSpace:

    def __init__(self, n):
        self.n = n

    def contains(self, x):
        return x in range(self.n)

    def __repr__(self):
        return f"{[i for i in range(self.n)]}"

    def __iter__(self):
        return iter([i for i in range(self.n)])

    def sample(self):
        return np.random.randint(self.n)


class DiscreteStateSpace:

    def __init__(self, states):
        self.states = states
        self.n = len(states)

    def __repr__(self):
        return f"{self.states}"

    def __iter__(self):
        return iter(self.states)

    def sample(self):
        return self.states[np.random.randint(self.n)]


class CustomBlackjackEnv(BlackjackEnv):

    def __init__(self, sab=True):
        super().__init__(sab=sab)
        self.player_sum_values = range(4, 32)  # Player's sum can range from 4 to 31
        self.dealer_showing_values = range(1, 11)  # Dealer's showing card ranges from 1 (Ace) to 10
        self.usable_ace_values = [False, True]
        self.state_space = DiscreteStateSpace([
            (player_sum, dealer_showing, usable_ace)
            for player_sum in self.player_sum_values
            for dealer_showing in self.dealer_showing_values
            for usable_ace in self.usable_ace_values
        ])
        self.action_space = DiscreteActionSpace(2)  # 0 for stick, 1 for hit

    def reset(self, observation=None):
        super().reset()
        if observation:
            player_total, dealer_showing, usable_ace = observation
            if usable_ace:
                self.player = [6, 1] if player_total == 17 else [player_total - 11, 1]
            else:
                self.player = [player_total - 10, 10]
            self.dealer = [dealer_showing, np.random.randint(1, 11)]
        return self._get_obs()

    def step(self, action):
        next_state, reward, terminated, _, _  = super().step(action)
        return next_state, reward, terminated

    def render(self, show_dealer_hand=False):
        player_hand_str = [self.card_to_str(card) for card in self.player]
        dealer_hand_str = [self.card_to_str(card) for card in self.dealer]
        print(f"Player's hand: {player_hand_str} with sum: {sum_hand(self.player)}")
        print(f"Dealer's showing card: {self.card_to_str(self.dealer[0])}")
        if show_dealer_hand:
            print(f"Dealer's hand: {dealer_hand_str} with sum: {sum_hand(self.dealer)}")

    def card_to_str(self, card):
        if card == 1:
            return 'Ace'
        elif card in [11, 12, 13]:
            return {11: 'Jack', 12: 'Queen', 13: 'King'}[card]
        else:
            return str(card)
