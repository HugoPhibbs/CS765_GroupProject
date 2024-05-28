import random
import math


class BettingRound:

    def __init__(self, num_coins, max_bet, type = "greater_than_or_equal_to"):
        """
        A betting round

        :param num_coins: number of coins in the round
        :param num_heads: number of heads in this round for the player to win
        :param max_bet: maximum bet amount for the round
        :param type: type of betting round. E.g. "greater_than_or_equal_to", "less_than", "equal_to", for number of heads in a round
        """
        self.num_coins = num_coins
        self.max_bet = max_bet
        self.win = None # Whether the player won the round
        self.type = type
        self.__set_num_heads()
        self.__set_bet_amount()

    def __set_num_heads(self):
        if self.type == "greater_than_or_equal_to":
            self.num_heads = random.randint(1, self.num_coins - 1)
        elif self.type == "less_than":
            self.num_heads = random.randint(1, self.num_coins)
        elif self.type == "equal_to":
            self.num_heads = random.randint(0, self.num_coins)
        else:
            raise ValueError(f"Invalid type of betting round, type {self.type}")

    def __repr__(self):
        return f"n_coins: {self.num_coins}, n_heads: {self.num_heads}, p_win: {self.p_win()}, e_v: {self.expected_value()}, bet: {self.bet}, type: {self.type}"

    def expected_value(self) -> float:
        """
        Expected value of the round

        Uses E(X) = p_win * bet

        :param bet: bet amount
        :return: the expected value of the round
        """
        p_win = self.p_win()
        return self.bet * p_win + (-self.bet) * self.p_lose()

    def p_lose(self) -> float:
        """
        Probability of losing the round

        :return: the probability of losing the round
        """
        return 1 - self.p_win()

    def p_win(self) -> float:
        """
        Probability of winning the round

        Uses the combinations formula to calculate the probability of winning the round

        :return: the probability of winning the round
        """
        n = self.num_coins
        k = self.num_heads
        if self.type == "greater_than_or_equal_to":
            return self.__p_win_greater_than_or_equal_to()
        elif self.type == "less_than":
            return 1 - self.__p_win_greater_than_or_equal_to()
        elif self.type == "equal_to":
            return self.__dice_binomial(n, k)
        else:
            raise ValueError(f"Invalid type of betting round, type {self.type}")
    
    def __p_win_greater_than_or_equal_to(self):
        n = self.num_coins
        k = self.num_heads
        return sum([self.__dice_binomial(n, i) for i in range(k, n+1)])
    
    def __dice_binomial(self, n, k):
        """Chance of getting exactly k heads in n coin flips

        :param n: n coin flips
        :param k: k heads
        """
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

    def __set_bet_amount(self) -> int:
        """
        Randomly set a bet amount

        :return: int for a bet amount
        """
        self.bet = random.randint(0, self.max_bet)

    def simulate_round(self) -> int:
        """
        Play a round of the betting game
        :param bet: amount to bet
        :return: amount won or lost
        """
        p_res = random.random()

        if p_res < self.p_win():
            self.win = True
            return self.bet
        else:
            self.win = False
            return -self.bet
