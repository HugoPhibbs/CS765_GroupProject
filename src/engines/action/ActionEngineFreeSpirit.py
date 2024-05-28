from src.engines.action.ActionEngine import ActionEngine

class ActionEngineFreeSpirit(ActionEngine):
    
    @staticmethod
    def evaluate(agent, game, round):
        score = (round.p_win() - 0.3) + agent.emotion_state.happy * 1/3 - agent.emotion_state.sad * 1/6
        return score >= 0