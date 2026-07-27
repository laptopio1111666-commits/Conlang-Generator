import sys

sys.path.insert(0, "D:\\Linguistics\\Conlang Generator")

from engine.phoneme.consonant import Consonant,Voicing,PlaceSpecific,Manner
from engine.phoneme.vowel import Vowel,Voicing,Height,Backness,Roundness,Nasalization,Length

a = Vowel(Voicing.VOICED,Height.OPEN,Backness.CENTRAL,Roundness.UNROUNDED,Nasalization.UNNASALIZED,Length.LONG)

c = Consonant(Voicing.VOICELESS,PlaceSpecific.PALATAL,Manner.PLOSIVE)

print(a)
print(c)