from src.engines.emotion.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange
from src.agent.Agent import Agent
from src.game.BettingGame import BettingGame
from src.game.BettingRound import BettingRound
from abc import ABC, abstractmethod

class EmotionEngineFreeSpirit(EmotionEngine):
    @staticmethod
    def evaluate(game: BettingGame, round : BettingRound) -> EmotionChange:
        # Parameters can be static - set when initialising the game
        pass # TODO