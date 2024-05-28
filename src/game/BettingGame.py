import random
import time
import textwrap
from src.game.BettingRound import BettingRound
from src.agent.Agent import Agent


class BettingGame:

    def __init__(self, num_rounds=10, coins_per_round=3, starting_cash=100, max_bet_per_round=None, min_bet=5):
        self.num_rounds = num_rounds
        self.coins_per_round = coins_per_round
        self.starting_cash = starting_cash
        self.max_bet_per_round = max_bet_per_round if max_bet_per_round is not None else starting_cash // 2
        self.min_bet = min_bet
        self.curr_round = 0
        self.past_rounds = []

    def __repr__(self):
        pass  # TODO

    def query_winstreak(self):
        count = 0
        for _ in range(len(self.past_rounds) - 1, -1, -1):
            if self.past_rounds[count].win:
                count += 1
            else:
                break
        return count

    def query_lossstreak(self):
        count = 0
        for _ in range(len(self.past_rounds) - 1, -1, -1):
            if not self.past_rounds[count].win:
                count += 1
            else:
                break
        return count

    def query_win_count(self):
        count = 0
        for round in self.past_rounds:
            if round.win:
                count += 1
        return count

    def query_loss_count(self):
        count = 0
        for round in self.past_rounds:
            if not round.win:
                count += 1
        return count

    def query_win_percentage(self):
        if len(self.past_rounds) == 0:
            return 0
        return self.query_win_count() / len(self.past_rounds)

    def most_recent_round_won(self):
        return self.past_rounds[-1].win

    def reset_game(self) -> None:
        """
        Resets the game

        :return: None
        """
        self.curr_round = 0
        self.past_rounds = []

    def generate_next_round(self, curr_agent_cash=float("inf")) -> BettingRound:
        """
        Generates a new betting round

        :return:
        """
        max_bet = min(self.max_bet_per_round, curr_agent_cash)  # Player can't bet more than they have

        return BettingRound(self.coins_per_round,
                            max_bet=max_bet)

    def play_game(self, agent: Agent, skip_time_outs=False) -> int:
        """
        Plays the game

        :param player: Player to play the game
        :return: the final cash amount of the player after the game
        """
        print("Starting the game")
        print(
            f"Params: num_rounds: {self.num_rounds}, coins_per_round: {self.coins_per_round}, starting_cash: {self.starting_cash}")

        curr_cash = self.starting_cash

        num_rounds_taken = 0

        for _ in range(self.num_rounds):

            if curr_cash < self.min_bet:
                print("Not enough cash to play the next round")
                break

            if curr_cash <= 0:
                print("Player has no more cash to play the game")
                break

            self.curr_round += 1

            print(f"Round: {self.curr_round}")
            betting_round = self.generate_next_round(curr_agent_cash=curr_cash)
            print(betting_round)
            if not skip_time_outs: time.sleep(2)

            print("Asking the player if they want to take the bet")
            take_round = agent.play_round(betting_round, game=self)

            if take_round:
                print("Taking the bet")
                print("Simulating the round")
                cash_win = betting_round.simulate_round()
                if not skip_time_outs: time.sleep(2)

                if betting_round.is_win():
                    print(f"Won the round: {cash_win}")
                else:
                    print(f"Lost the round: {cash_win}")

                self.past_rounds.append(betting_round)
                curr_cash += cash_win
                num_rounds_taken += 1
            else:
                print("Not taking the bet")
                continue

            agent.update_agent(betting_round, self)

            print(f"Current cash: {curr_cash}")

        self.__print_game_summary(curr_cash, self.curr_round, num_rounds_taken, agent)

        return curr_cash

    def __print_game_summary(self, curr_cash, rounds_played, num_rounds_taken, agent):
        print(
            textwrap.dedent(
                f"""
                Summary:
                Player Type: {repr(agent.agent_type)}
                Rounds: {rounds_played}
                Rounds taken: {num_rounds_taken}
                Player cash (start/final): {self.starting_cash}/{curr_cash}
                Wins: {self.query_win_count()}
                Losses: {self.query_loss_count()}
                Win percentage: {self.query_win_percentage():.2f}
                """
            )
        )

