from src.engines.emotion.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange

class EmotionEngineFreeSpirit(EmotionEngine):
    @staticmethod
    def evaluate(game, round) -> EmotionChange:
        change = EmotionChange()
        if game.most_recent_round_won():
            change.happy_incr(2)
            change.fearful_incr(-2)
            change.sad_incr(-1)
        else:
            change.happy_incr(-1)
            change.sad_incr(1)
            change.fearful_incr(1)
        change.happy_incr(0.5 * game.query_winstreak() - 0.1 * game.query_lossstreak())
        change.sad_incr(0.1 * game.query_lossstreak() - 0.5 * game.query_winstreak())
        return change