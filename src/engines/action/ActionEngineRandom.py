from src.engines.action.ActionEngine import ActionEngine
import random


class ActionEngineRandom(ActionEngine):
    
    @staticmethod
    def evaluate(agent, game, round) -> bool:
        return random.random() < 0.5