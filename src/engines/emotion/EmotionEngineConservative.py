from src.engines.emotion.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange


class EmotionEngineConservative(EmotionEngine):
    @staticmethod
    def evaluate(game, round) -> EmotionChange:
        emotion_change = EmotionChange()
        if game.most_recent_round_won:
            emotion_change.fearful_incr(- 1 + game.query_loss_count() / 3)
            emotion_change.happy_incr(2 / (2 + game.query_loss_count()) * (1 + game.query_winstreak() / 5))
            emotion_change.sad_incr(-2 / (2 + game.query_loss_count()) * (1 + game.query_winstreak() / 5))
            emotion_change.angry_incr(-0.5)
        else:
            emotion_change.fearful_incr((1 + game.query_loss_count() / 3) * (1 + game.query_lossstreak() / 2))
            emotion_change.happy_incr(- 1 + 1 / 3)
            emotion_change.sad_incr(2)
            emotion_change.angry_incr(0.5)

        emotion_change.fearful += (game.query_loss_count() - game.query_win_count()) * 0.2

        return emotion_change
