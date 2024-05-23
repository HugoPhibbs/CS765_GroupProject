from src.agent.AgentType import AgentType
from customLogic import Statement

class EmotionMap: 

    """
        Maps a statement, to the emotion change of an agent (depending on the agent type)
    """

    def __init__(self, emotion_map) -> None:
        self.emotion_map = emotion_map

    def find_emotion_change(self, agent_type : AgentType, statement : Statement):
        return self.emotion_map[statement][agent_type]

    # def add_agent(self, agent_type, happy, sad, fearful, angry):
    #     if agent_type in self.emotion_map.keys():
    #         raise KeyError("Agent already mapped.")
        
    #     self.emotion_map[agent_type] = {"happy": happy, "sad": sad, "fearful": fearful, "angry": angry}
    
    # def query_agent_emotion(self, agent_type, emotion):
    #     return self.emotion_map[agent_type][emotion] 
    
    # def query_agent(self, agent_type):
    #     return self.emotion_map[agent_type]
    
    

emotion_map = {
    Conditional
}