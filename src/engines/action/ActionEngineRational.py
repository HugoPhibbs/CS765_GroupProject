from src.engines.action.ActionEngine import ActionEngine


class ActionEngineRational(ActionEngine):
    
    @staticmethod
    def evaluate(agent, game, round) -> bool:
        return round.expected_value() > 0