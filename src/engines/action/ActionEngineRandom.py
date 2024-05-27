from src.engines.action.ActionEngine import ActionEngine
import random


class ActionEngineRandom(ActionEngine):
    
    @staticmethod
    def evaluate(game, round) -> bool:
        return random.random() < 0.5