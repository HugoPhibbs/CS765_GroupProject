import random
import math


class BettingRound:
    win = None # Whether the player won the round

    def __init__(self, num_coins, num_heads, max_bet):
        """
        A betting round

        :param num_coins: number of coins in the round
        :param num_heads: number of heads in this round for the player to win
        :param max_bet: maximum bet amount for the round
        """
        self.num_coins = num_coins
        self.num_heads = num_heads
        self.max_bet = max_bet

    def __repr__(self):
        return f"n_coins: {self.num_coins}, n_heads: {self.num_heads}, p_win: {self.p_win()}, e_v: {self.expected_value()}, bet: {self.bet_amount()}"

    def expected_value(self, bet=1) -> float:
        """
        Expected value of the round

        Uses E(X) = p_win * bet

        :param bet: bet amount
        :return: the expected value of the round
        """
        p_win = self.p_win()
        return bet * p_win + (-bet) * (1 - p_win)

    def p_win(self) -> float:
        """
        Probability of winning the round

        Uses the combinations formula to calculate the probability of winning the round

        :return: the probability of winning the round
        """
        n = self.num_coins
        k = self.num_heads
        return math.comb(n, k) * (0.5 ** k) * (0.5 ** (n - k))

    def is_win(self) -> bool:
        """
        Whether the player won the round

        Raises an error if the round has not been played yet

        :return: boolean whether the player won the round
        """
        if self.win is None:
            raise ValueError("The round has not been played yet")
        return self.win

    def bet_amount(self) -> int:
        """
        Randomly generate a bet amount

        :return: int for a bet amount
        """
        return random.randint(1, self.max_bet)

    def simulate_round(self) -> int:
        """
        Play a round of the betting game
        :param bet: amount to bet
        :return: amount won or lost
        """
        bet = self.bet_amount()
        trials = [random.choice(["H", "T"]) for _ in range(self.num_heads)]
        heads_count = trials.count("H")
        if heads_count > self.num_heads:
            self.win = True
            return bet
        else:
            self.win = False
            return -bet
