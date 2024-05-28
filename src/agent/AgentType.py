from enum import Enum

class AgentType(Enum):
    RATIONAL = 0
    FREE_SPIRIT = 1
    CONSERVATIVE = 2
    TEMPERAMENTAL = 3
    RANDOM = 4

    def __repr__(self):
        return self.name