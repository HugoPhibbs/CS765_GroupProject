from src.agent.Agent import Agent
from src.agent.AgentType import AgentType
from src.game.BettingGame import BettingGame

rationalAgent = Agent(AgentType.TEMPERAMENTAL)
game = BettingGame(30, 10, 100)

game.play_game(rationalAgent, skip_time_outs=True)