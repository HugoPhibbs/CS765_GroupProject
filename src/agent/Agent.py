from src.game.BettingRound import BettingRound
from src.game.BettingGame import BettingGame
from customLogic import Statement, StatementList, AtomicStatement
from State import State
from src.agent.EmotionState import EmotionState
from src.agent.AgentType import AgentType
from src.StatementEngines.StatementEmotionEngine import StatementEmotionEngine
from src.StatementEngines.StatementActionEngine import StatementActionEngine


class Agent:
    
    def __init__(self, agent_type: AgentType, emotion_state : EmotionState):
        """
        A player object
        """
        self.agent_type = agent_type 
        self.emotion_state = emotion_state

    def update_agent(self, round : BettingRound, game: BettingGame) -> None:
        """
        Updates the internal state the agent based on the current game state
        
        """
        emotionChange = StatementEmotionEngine.evaluate(self, game, round)
        self.emotion_state.update(emotionChange)

    def play_round(self, round : BettingRound, game: BettingGame) -> bool:
        """
        4. Pass in current game state, current betting around, and the game into a statements engine again
        5. This time the statement engine evaluates:
            * Whether the player should take the bet or not

        6. Finally return whether the player should take the bet or not
        7. This output then is used to evaluate and change the game state. Rinse and repeat.
        """

        return StatementActionEngine.evaluate(self, game, round)


        #
        # Take in the game object and evaluate the game

        # Change the internal emotional state oƒ agent based on their personality and the state of the game

        # Then return a boolean that they are going to take the bet or not