from engine.phoneme.features import Voicing, PlaceSpecific, Manner

class Consonant:
    def __init__(self, voicing, place, manner):
        self.place = place
        self.manner = manner
        self.voicing = voicing

    def __eq__(self,other):
        return (self.place == other.place  and
                self.manner == other.manner and 
                self.voicing == other.voicing)
    def __str__(self):
        return f"{self.voicing.name},{self.place.name},{self.manner.name}"
    def __repr__(self):
        return f"[{self.voicing.name},{self.place.name},{self.manner.name}]"