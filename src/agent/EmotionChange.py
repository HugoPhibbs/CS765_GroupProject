class EmotionChange:

    def __init__(self, happy=0, sad=0, fearful=0, angry=0) -> None:
        self.happy = happy
        self.sad = sad
        self.fearful = fearful
        self.angry = angry
    
    def happy_incr(self, happy_increment=0):
        self.happy += happy_increment
        self.happy = self.__cap_emotion(self.happy)

    def sad_incr(self, sad_increment=0):
        self.sad += sad_increment
        self.sad = self.__cap_emotion(self.sad)

    def fearful_incr(self, fearful_increment=0):
        self.fearful = fearful_increment
        self.fearful = self.__cap_emotion(self.fearful)

    def angry_incr(self, angry_increment=0):
        self.angry = angry_increment
        self.angry = self.__cap_emotion(self.angry)
    
    def __cap_emotion(self, emotion):
        if emotion <= 0:
            return 0
        elif emotion > 10:
            return 10
        else:
            return emotion