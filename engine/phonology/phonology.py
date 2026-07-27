
class Phonology:
    def __init__(self, allow_duplicates = False):
        self.consonants     = []
        self.vowels         = []      
        self.allow_duplicates = allow_duplicates
    
    def __str__(self):
        return f"Consonants: {self.consonants} \nVowels: {self.vowels}"

    def __repr__(self):
        return f"Consonants: {self.consonants} \nVowels: {self.vowels}"  

    def def_phonology(self,consonants,vowels):
        self.consonants = list(consonants)
        self.vowels     = list(vowels)

    def add_consonant(self,consonant,allow_duplicates=None):
        allow = self.allow_duplicates if allow_duplicates is None else allow_duplicates
        if allow or consonant not in self.consonants:
            self.consonants.append(consonant)

    def add_vowel(self,vowel,allow_duplicates=None):    
        allow = self.allow_duplicates if allow_duplicates is None else allow_duplicates
        if allow or vowel not in self.vowels:
            self.vowels.append(vowel)

    def remove_consonant(self, consonant):
        if consonant in self.consonants:    
            self.consonants.remove(consonant)
    
    def remove_vowel(self, vowel):
        if vowel in self.vowels:
            self.vowels.remove(vowel)

    def has_consonant(self, consonant):
        return consonant in self.consonants

    def has_vowel(self,vowel):
        return vowel in self.vowels

    def num_vowels(self):
        return len(self.vowels)

    def num_consonants(self):
        return len(self.consonants)