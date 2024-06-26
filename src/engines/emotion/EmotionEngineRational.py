from src.agent.EmotionChange import EmotionChange
from src.engines.emotion.EmotionEngine import EmotionEngine

class EmotionEngineRational(EmotionEngine):

    @staticmethod
    def evaluate(game, round) -> EmotionChange:
        return EmotionChange(0, 0, 0, 0)