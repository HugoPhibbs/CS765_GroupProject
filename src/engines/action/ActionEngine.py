from src.agent.Agent import Agent
from src.game.BettingGame import BettingGame
from src.game.BettingRound import BettingRound
from abc import ABC, abstractmethod

class ActionEngine(ABC):

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def evaluate(agent : Agent, game : BettingGame, round : BettingRound) -> bool:
        pass # TODO