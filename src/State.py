class State:

    def __init__(self, happy=0, sad=0, fearful=0, angry=0):
        self.emotions = {}
        self.emotions["happy" ]= happy
        self.emotions["sad"] = sad
        self.emotions["fearful"] = fearful
        self.emotions["angry"] = angry

    def adjust_state(self, change_happy, change_sad, change_fearful, change_angry):
        State.emotions["happy"] += change_happy
        State.emotions["sad"] += change_sad
        State.emotions["fearful"] += change_fearful
        State.emotions["angry"] += change_angry

    def evaluate_state(self):
        pass 

    def all_emotions_str(self) -> list:
        return self.emotions.keys()