from src.engines.action import ActionEngineConservative, ActionEngineFreeSpirit, ActionEngineRational, ActionEngineTempermental
from src.game.BettingRound import BettingRound
from src.game.BettingGame import BettingGame
from customLogic import Statement, StatementList, AtomicStatement
from State import State
from src.agent.EmotionState import EmotionState
from src.agent.AgentType import AgentType
from src.engines.emotion.EmotionEngine import EmotionEngine
from src.engines.action.ActionEngine import ActionEngine

from src.engines.emotion.EmotionEngineRational import EmotionEngineRational
from src.engines.emotion.EmotionEngineConservative import EmotionEngineConservative
from src.engines.emotion.EmotionEngineTempermental import EmotionEngineTempermental
from src.engines.emotion.EmotionEngineFreeSpirit import EmotionEngineFreeSpirit


class Agent:
    
    def __init__(self, agent_type: AgentType, emotion_state : EmotionState):
        """
        A player object
        """
        self.agent_type = agent_type 
        self.emotion_state = emotion_state
        self.set_engines()

    def set_engines(self):
        if self.agent_type == 0:
            self.emotion_engine = EmotionEngineRational
            self.action_engine = ActionEngineRational
        elif self.agent_type == 1:
            self.emotion_engine = EmotionEngineFreeSpirit
            self.action_engine = ActionEngineFreeSpirit
        elif self.agent_type == 2:
            self.emotion_engine = EmotionEngineConservative
            self.action_engine = ActionEngineConservative
        elif self.agent_type == 3:
            self.emotion_engine = EmotionEngineTempermental
            self.action_engine = ActionEngineTempermental
        elif self.agent_type == 4:
            # self.emotion_engine = EmotionEngineRandom
            # self.action_engine = ActionEngineRandom
            pass
        else:
            raise ValueError(f"Invalid agent type {self.agent_type}")


    def update_agent(self, round : BettingRound, game: BettingGame) -> None:
        """
        Updates the internal state the agent based on the current game state
        
        """
        emotionChange = self.emotion_engine.evaluate(self, game, round)
        self.emotion_state.update(emotionChange)

    def play_round(self, round : BettingRound, game: BettingGame) -> bool:
        """
        4. Pass in current game state, current betting around, and the game into a statements engine again
        5. This time the statement engine evaluates:
            * Whether the player should take the bet or not

        6. Finally return whether the player should take the bet or not
        7. This output then is used to evaluate and change the game state. Rinse and repeat.
        """

        return self.action_engine.evaluate(self, game, round)


        #
        # Take in the game object and evaluate the game

        # Change the internal emotional state oƒ agent based on their personality and the state of the game

        # Then return a boolean that they are going to take the bet or not