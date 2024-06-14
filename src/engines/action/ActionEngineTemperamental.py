from src.engines.action.ActionEngine import ActionEngine


class ActionEngineTemperamental(ActionEngine):
    
    @staticmethod
    def evaluate(agent, game, round):
        """
        Returns a boolean indicating whether the agent will take the current bet or not

        :param agent: The agent taking the action
        :param game: The current game being played
        :param round: The current round being played

        :return: A boolean indicating whether the agent will take the current bet or not
        """
        chance = 0.5

        if agent.emotion_state.angry >= 5:
            chance -= 0.1 * game.query_loss_count()
        
        if agent.emotion_state.happy >= 5:
            chance += 0.1 * game.query_winstreak() + 1 * game.query_win_percentage()

        if agent.emotion_state.sad >= 5:
            chance -= 0.1 * game.query_loss_count()

        if agent.emotion_state.fearful == 10:
            return False

        elif agent.emotion_state.fearful >= 5:
            chance -= 0.1 * game.query_lossstreak()
        
        return chance > 0.5



