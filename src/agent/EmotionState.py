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