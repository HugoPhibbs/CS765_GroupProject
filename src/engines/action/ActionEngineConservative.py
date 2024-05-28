from src.engines.action.ActionEngine import ActionEngine


class ActionEngineConservative(ActionEngine):

    @staticmethod
    def evaluate(agent, game, round) -> bool:
        no_bet = (agent.emotion_state.fearful * 0.8 + agent.emotion_state.sad * 0.2) * (1 + round.p_lose())
        yes_bet = (- agent.emotion_state.fearful * 0.2 + agent.emotion_state.happy * 0.5 + (10 - agent.emotion_state.sad) * 0.5) * (round.expected_value())
        return yes_bet > no_bet
        #return False # TODO