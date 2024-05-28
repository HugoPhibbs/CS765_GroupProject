from src.engines.emotion.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange

class EmotionEngineTempermental(EmotionEngine):
    @staticmethod
    def evaluate(game, round) -> EmotionChange:
        emotion_change = EmotionChange()
        if game.most_recent_round_won:
            emotion_change.fearful -= 2 + game.query_loss_count() / 5
            emotion_change.happy += (3 / (2 + game.query_loss_count())) * (2 + game.query_winstreak() / 5)
            emotion_change.sad -= 3 / (2 + game.query_loss_count()) * (1 + game.query_winstreak() / 5)
            emotion_change.angry -= 1
        else:
            emotion_change.fearful += (1 + game.query_loss_count() / 3) 
            emotion_change.happy -= 2 + 1/3
            emotion_change.sad += 2
            emotion_change.angry += 3


        return emotion_change