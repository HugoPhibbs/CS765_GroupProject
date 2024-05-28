from src.engines.emotion.EmotionEngine import EmotionEngine
from src.agent.EmotionChange import EmotionChange


class EmotionEngineTemperamental(EmotionEngine):

    @staticmethod
    def evaluate(game, round) -> EmotionChange:
        """
        Determines the emotion change for a temperamental agent based on the game and round
        :param game: current game being played
        :param round: current round being played
        :return: An EmotionChange object representing the change in emotions
        """
        emotion_change = EmotionChange()

        if game.most_recent_round_won:
            emotion_change.fearful_incr(-2 + game.query_loss_count() / 5)
            emotion_change.happy_incr(3 / (2 + game.query_loss_count()) * (2 + game.query_winstreak() / 5))
            emotion_change.sad_incr(-3 / (2 + game.query_loss_count()) * (1 + game.query_winstreak() / 5))
            emotion_change.angry_incr(-1)
        else:
            emotion_change.fearful_incr((1 + game.query_loss_count() / 3))
            emotion_change.happy_incr(- 2 + 1 / 3)
            emotion_change.sad_incr(2)
            emotion_change.angry_incr(3)

        return emotion_change
