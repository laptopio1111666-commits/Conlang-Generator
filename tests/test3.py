import sys
sys.path.insert(0, "D:\\Linguistics\\Conlang Generator")

from engine.phonology.phonology import phonology
from engine.phoneme.consonant import Consonant,Voicing,PlaceSpecific,Manner
from engine.phoneme.vowel import Vowel,Voicing,Height,Backness,Roundness,Nasalization,Length

n = phonology()
n.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.BILABIAL,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.ALVEOLAR,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.PALATAL,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICELESS,PlaceSpecific.VELAR,Manner.PLOSIVE))

n.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.BILABIAL,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.ALVEOLAR,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.PALATAL,Manner.PLOSIVE))
n.add_consonant(Consonant(Voicing.VOICED,PlaceSpecific.VELAR,Manner.PLOSIVE))


print(n.consonants)
print(n)