from engine.phoneme.features import Voicing, Height, Backness, Roundness, Nasalization, Length


class Vowel:
    def __init__(self,voicing,height,backness,roundness,nasalization,length):
        self.voicing = voicing
        self.height = height
        self.backness = backness
        self.roundness = roundness
        self.nasalization = nasalization
        self.length = length

    def __str__(self):
        return f"{self.voicing.name},{self.height.name},{self.backness.name},{self.roundness.name},{self.nasalization.name},{self.length.name}"

    def __repr__(self):
        return f"[{self.voicing.name},{self.height.name},{self.backness.name},{self.roundness.name},{self.nasalization.name},{self.length.name}]"

    def __eq__(self, other):
        return (self.height == other.height and
            self.backness == other.backness and
            self.roundness == other.roundness and
            self.nasalization == other.nasalization and
            self.length == other.length and
            self.voicing == other.voicing)