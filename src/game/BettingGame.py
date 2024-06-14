import random
import time
import textwrap
from src.game.BettingRound import BettingRound
from src.agent.Agent import Agent


class BettingGame:

    def __init__(self, num_rounds=10, coins_per_round=3, starting_cash=100, max_bet_per_round=None, min_bet=5, round_type="greater_than_or_equal_to"):
        self.num_rounds = num_rounds
        self.coins_per_round = coins_per_round
        self.starting_cash = starting_cash
        self.max_bet_per_round = max_bet_per_round if max_bet_per_round is not None else starting_cash // 2
        self.min_bet = min_bet
        self.curr_round = 0
        self.past_rounds = []
        self.round_type = round_type

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
                            max_bet=max_bet, 
                            type=self.round_type)

    def play_game(self, agent: Agent, skip_time_outs=False) -> int:
        """
        Plays the game

        :param player: Player to play the game
        :return: the final cash amount of the player after the game
        """
        self.__print_game_intro(agent)

        print(f"\n{self.__bold_str("Starting the game")}")

        curr_cash = self.starting_cash

        num_rounds_taken = 0

        for _ in range(self.num_rounds):

            print("-" * 50)
            if not skip_time_outs: time.sleep(0.5)

            if curr_cash < self.min_bet:
                print("Not enough cash to play the next round")
                break

            if curr_cash <= 0:
                print("Agent has no more cash to play the game")
                break

            self.curr_round += 1

            round_str = f"Round: {self.curr_round}/{self.num_rounds}"

            print(f"\n{self.__bold_str(round_str)}\n")

            print(agent.emotion_state.__repr__() + "\n")

            betting_round = self.generate_next_round(curr_agent_cash=curr_cash)
            print(betting_round)
            if not skip_time_outs: time.sleep(0.5)

            print("Asking the agent if they want to take the bet")
            if not skip_time_outs: time.sleep(0.5)
            take_round = agent.play_round(betting_round, game=self)

            if take_round:
                print(f"Agent {self.__bold_str("is")} taking the bet")
                print("Simulating the round")
                cash_win = betting_round.simulate_round()
                if not skip_time_outs: time.sleep(0.5)

                if betting_round.is_win():
                    print(f"{self.__bold_str("Won")} the round, won {cash_win}")
                else:
                    print(f"{self.__bold_str("Lost")} the round, lost {-cash_win}")

                self.past_rounds.append(betting_round)
                curr_cash += cash_win
                num_rounds_taken += 1
            else:
                print(f"Agent {self.__bold_str("not")} taking the bet")

                print(f"\nCurrent cash: {curr_cash}")

                continue

            agent.update_agent(betting_round, self)

            print(f"\nCurrent cash: {curr_cash}")

        self.__print_game_summary(curr_cash, self.curr_round, num_rounds_taken, agent)

        return curr_cash
    
    def __bold_str(self, s):
        return f"\033[1m{s}\033[0m"
    
    def __print_game_intro(self, agent):
        print(
            textwrap.dedent(
                f"""
                {self.__bold_str("Parameters")}
                Number of rounds: {self.num_rounds}, 
                Coins per round: {self.coins_per_round}, 
                Starting_cash: {self.starting_cash}
                Agent Type: {repr(agent.agent_type)}
                Round Types: {self.round_type}
                """
            )
        )

    def __print_game_summary(self, curr_cash, rounds_played, num_rounds_taken, agent):
        print(
            textwrap.dedent(
                f"""
                {"-" * 50}
                {self.__bold_str("Game Summary")}:
                Agent Type: {repr(agent.agent_type)}
                Rounds: {rounds_played}
                Rounds taken: {num_rounds_taken}
                Agent cash (start/final): {self.starting_cash}/{curr_cash}
                Wins: {self.query_win_count()}
                Losses: {self.query_loss_count()}
                Win percentage: {self.query_win_percentage():.2f}
                """
            )
        )

