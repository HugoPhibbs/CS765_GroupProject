from src.agent.EmotionChange import EmotionChange
from abc import ABC, abstractmethod

class EmotionEngine(ABC):

    def __init__(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def evaluate(game, round) -> EmotionChange:
        # Parameters can be static - set when initialising the game
        pass # TODO

