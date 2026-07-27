from engine.phoneme.consonant import Consonant
from engine.phoneme.vowel import Vowel


class Phonotactic_Slot:
    def __init__(self, index, slot_type):
        self.slot_type = slot_type  
        self.index = index
        self.valid = []             

class Phonotactics:
    def __init__(self, syllable_structure, phonology):
        self.syllable_structure = syllable_structure
        self.phonology = phonology
        self.slots = {}

        pattern = syllable_structure.human_readable_arranged()
        for i, slot_type in enumerate(pattern):
            self.slots[i] = Phonotactic_Slot(i, slot_type)

    def add_to_slot(self, index, phoneme):
        if index not in self.slots:
            return
        if isinstance(phoneme, Consonant):
            if phoneme in self.phonology.consonants:
                if phoneme not in self.slots[index].valid:
                    self.slots[index].valid.append(phoneme)
        elif isinstance(phoneme, Vowel):
            if phoneme in self.phonology.vowels:
                if phoneme not in self.slots[index].valid:
                    self.slots[index].valid.append(phoneme)
    
    def remove_from_slot(self, index, phoneme):
        if index not in self.slots:
            return
        if phoneme in self.slots[index].valid:
            self.slots[index].valid.remove(phoneme)
    