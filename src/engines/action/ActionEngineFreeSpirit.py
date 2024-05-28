from src.engines.action.ActionEngine import ActionEngine


class ActionEngineFreeSpirit(ActionEngine):

    @staticmethod
    def evaluate(agent, game, round):
        score = (
                (round.p_win() - 0.2)
                + agent.emotion_state.happy * 1 / 3
                - agent.emotion_state.sad * 1 / 4
                - agent.emotion_state.fearful * 1 / 5
        )
        return score >= 0
