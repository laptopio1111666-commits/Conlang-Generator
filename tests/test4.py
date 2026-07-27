import sys
sys.path.insert(0, "D:\\Linguistics\\Conlang Generator")

from engine.phoneme.features import Voicing, PlaceSpecific, Manner, Height, Backness, Roundness, Nasalization, Length
from engine.phoneme.consonant import Consonant
from engine.phoneme.vowel import Vowel
from engine.phonology.phonology import Phonology
from engine.syllable_structure.syllable_structure import Syllable_Structure
from engine.phonotactics.phonotactics import Phonotactics

P1 = Phonology()

P1.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.BILABIAL,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.ALVEOLAR,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.PALATAL,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.VELAR,Manner.PLOSIVE))

P1.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.BILABIAL,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.ALVEOLAR,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.PALATAL,Manner.PLOSIVE))
P1.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.VELAR,Manner.PLOSIVE))

S1 = Syllable_Structure(4,2,3)

Ph1 = Phonotactics(S1,P1)

Ph1.add_to_slot(0, Consonant(Voicing.VOICELESS, PlaceSpecific.BILABIAL, Manner.PLOSIVE))

print(Ph1.slots[4].valid)