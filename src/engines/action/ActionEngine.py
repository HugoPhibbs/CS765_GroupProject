from abc import ABC, abstractmethod

class ActionEngine(ABC):

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def evaluate(agent, game, round) -> bool:
        pass # TODO