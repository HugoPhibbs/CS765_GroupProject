from src.agent.Agent import Agent
from src.agent.EmotionChange import EmotionChange
from src.engines.emotion.EmotionEngine import EmotionEngine
from src.game.BettingGame import BettingGame
from src.game.BettingRound import BettingRound

class EmotionEngineRational(EmotionEngine):

    @staticmethod
    def evaluate(game: BettingGame, round: BettingRound) -> EmotionChange:
        return EmotionChange(0, 0, 0, 0)