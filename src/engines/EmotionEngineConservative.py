from src.engines.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange
from src.agent.Agent import Agent
from src.game.BettingGame import BettingGame
from src.game.BettingRound import BettingRound
from abc import ABC, abstractmethod

class EmotionEngineConservative(EmotionEngine):
    @staticmethod
    def evaluate(agent : Agent, game: BettingGame, round : BettingRound) -> EmotionChange:
        for statement in agent.