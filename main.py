from src.agent.Agent import Agent
from src.agent.AgentType import AgentType
from src.game.BettingGame import BettingGame

# Creating an Agent
# agent = Agent(agent_type = AgentType.RATIONAL)
# agent = Agent(agent_type = AgentType.CONSERVATIVE)
agent = Agent(agent_type = AgentType.TEMPERAMENTAL)

# Creating a game instance
game = BettingGame(
    num_rounds = 10, 
    coins_per_round = 10,
    starting_cash =  100
    )

# Playing the game
game.play_game(
    agent=agent, 
    skip_time_outs=False
    )

