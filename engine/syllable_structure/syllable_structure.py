
class Syllable_Structure:
    def __init__ (self, onset_len, nucleus_len, coda_len):
        self.onset_len = onset_len
        self.nucleus_len = nucleus_len
        self.coda_len = coda_len
    
    def total_len(self):
        return self.onset_len + self.nucleus_len + self.coda_len

    def human_readable(self):
        return "C" * self.onset_len + "V" * self.nucleus_len + "C" * self.coda_len
    
    def human_readable_arranged(self):
        return "O" * self.onset_len + "N" * self.nucleus_len + "C" * self.coda_len