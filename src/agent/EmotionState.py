class EmotionState:

    def __init__(self, happy=0, sad=0, angry=0, fearful=0):
        self.happy = happy
        self.sad = sad
        self.angry = angry
        self.fearful = fearful

    def update(self, emotion_change):
        self.happy += emotion_change.happy
        self.sad += emotion_change.sad
        self.angry += emotion_change.angry
        self.fearful += emotion_change.fearful

    def __repr__(self):
        return f"EmotionState(happy={self.happy:.2f}, sad={self.sad:.2f}, angry={self.angry:.2f}, fearful={self.fearful:.2f})"