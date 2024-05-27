from src.engines.action.ActionEngine import ActionEngine


class ActionEngineConservative(ActionEngine):

    @staticmethod
    def evaluate(game, round) -> bool:
        return False # TODO