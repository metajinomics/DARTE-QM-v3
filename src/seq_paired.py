
class Seq_paired(object):
    def __init__(self):
        self.r1 = []
        self.r2 = []

    def __call__(self):
        ""

    def add(self, seq1, seq2):
        self.r1.append(seq1)
        self.r2.append(seq2)

    def list_add(self, seq1, seq2):
        self.r1.extend(seq1)
        self.r2.extend(seq2)

    def get(self):
        return self.r1, self.r2
