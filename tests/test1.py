import sys

sys.path.insert(0, "D:\\Linguistics\\Conlang Generator")

from engine.phoneme.consonant import Consonant, PlaceSpecific, Manner, Voicing
from engine.syllable_structure.syllable_structure import Syllable_Structure
from engine.phonology.phonology import phonology

p = Consonant(PlaceSpecific.BILABIAL, Manner.PLOSIVE, Voicing.VOICELESS)
syl_strut = Syllable_Structure(3,2,1)
M = phonology()
print(type(M.consonants))

print(p.place,end=" ")
print(p.place.value)
print(p.manner,end=" ")
print(p.manner.value)
print(p.voicing,end=" ")
print(p.voicing.value)

print(syl_strut.human_readable_arranged(), syl_strut.human_readable())

b1 = Consonant(Voicing.VOICED,PlaceSpecific.BILABIAL,Manner.PLOSIVE)
b2 = Consonant(Voicing.VOICED,PlaceSpecific.BILABIAL,Manner.PLOSIVE)

print(b1 == b2)