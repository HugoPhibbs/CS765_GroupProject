import random
import time
from src.game.BettingRound import BettingRound
from src.Agent.Agent import Agent


class BettingGame:
    curr_round = 0
    past_rounds = []

    def __init__(self, num_rounds=10, coins_per_round=3, starting_cash=100, max_bet_per_round=None):
        self.num_rounds = num_rounds
        self.coins_per_round = coins_per_round
        self.starting_cash = starting_cash
        self.max_bet_per_round = max_bet_per_round if not max_bet_per_round else starting_cash // 2

    def __repr__(self):
        pass  # TODO

    def reset_game(self) -> None:
        """
        Resets the game

        :return: None
        """
        self.curr_round = 0
        self.past_rounds = []

    def generate_next_round(self) -> BettingRound:
        """
        Generates a new betting round

        :return:
        """
        self.curr_round += 1
        return BettingRound(self.coins_per_round, random.randint(0, self.coins_per_round),
                            max_bet=self.max_bet_per_round)

    def play_game(self, agent: Agent) -> int:
        """
        Plays the game

        :param player: Player to play the game
        :return: the final cash amount of the player after the game
        """
        print("Starting the game")
        print(
            f"Params: num_rounds: {self.num_rounds}, coins_per_round: {self.coins_per_round}, starting_cash: {self.starting_cash}")

        curr_cash = self.starting_cash

        for _ in range(self.num_rounds):
            print(f"Round: {self.curr_round}")
            betting_round = self.generate_next_round()
            print(betting_round)
            time.sleep(2)

            print("Asking the player if they want to take the bet")
            take_round = agent.play_round(betting_round, past_rounds=self.past_rounds)

            if take_round:
                print("Taking the bet")
                print("Simulating the round")
                cash_win = betting_round.simulate_round()
                time.sleep(2)

                if betting_round.is_win():
                    print(f"Won the round: {cash_win}")
                else:
                    print(f"Lost the round: {cash_win}")

                self.past_rounds.append(betting_round)
                curr_cash += cash_win
            else:
                print("Not taking the bet")
                continue

            agent.update_agent(betting_round, self)

            self.curr_round += 1

        return curr_cash
