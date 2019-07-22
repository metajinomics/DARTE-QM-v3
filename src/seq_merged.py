
class Seq_merged(object):
    def __init__(self):
        self.r1 = []

    def __call__(self):
        ""

    def add(self, seq1):
        self.r1.append(seq1)

    def list_add(self, seq1):
        self.r1.extend(seq1)

    def get(self):
        return self.r1
