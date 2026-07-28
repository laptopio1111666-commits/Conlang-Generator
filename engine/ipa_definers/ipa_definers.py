

class ipa_vowel:
    def __init__(self,vowel_bool,voicing,height,backness,roundness,nasalization,length):
        self.vowel_bool = vowel_bool
        self.voicing = voicing
        self.height = height
        self.backness = backness
        self.roundness = roundness
        self.nasalization = nasalization
        self.length = length

class ipa_consonant:
    def __init__(self,voicing,manner,place):
        self.place = place
        self.manner = manner
        self.voicing = voicing