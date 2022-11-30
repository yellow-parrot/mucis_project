from FoxDot import *
class Sequence:
#
    def __init__(self):
        self.list = [[0, 1, 2, 3, 4], [0, 3, 4]] #34
#
    def mute(self):
        p2.stop()
#
    def seq(self, chord, n):
        if n == 0:#123_
            chord1 = list("")
            for i in range(len(chord)):
                chord1 += list(chord[i]) + [15]
            return (chord1, 1)
        if n == 1:#12321_
            chord1 = list("")
            for i in range(len(chord)):
                l1 = list(chord[i])[:-1:]
                l1 = l1[::-1]
                chord1 += list(chord[i]) + l1 + [15]
            return (chord1, 0)
        if n == 2:#12378_
            chord1 = list("")
            for i in range(len(chord)):
                l1 = list(P(list(chord[i])[1::]) + 0)
                chord1 += list(chord[i]) + l1 + [15]
            return (chord1, 0)
        if n == 3:#12(345)_
            chord1 = list("")
            for i in range(len(chord)):
                l1 = list(P(list(chord[i])[1::]) + 0)
                chord1 += list(chord[i]) + l1 + [15]
            return (chord1, 1)
        if n == 4:#(123)45_
            chord1 = list("")
            for i in range(len(chord)):
                l1 = []
                l1.append(tuple(list(chord[i])[:1:] + list(P(list(chord[i])[1::]) + 0)))
                chord1 += l1 + list(chord[i])[:-1:] + [15]
            return (chord1, 1)
#
    def play(self, multiplicity, chord, n):
#
        n1 = self.list[multiplicity - 3][n]
        seq1, r = self.seq(chord, n1)
#
        p2 >> keys(list(P(seq1) - 4), dur = [1/2] * (len(seq1) // len(chord) - 1) + [rest(1/2 * ((r + multiplicity) % 2))], amp = 1.0 * 3)
#
    def number(self, multiplicity):
        if multiplicity == 3:
            return len(self.list[0])
        if multiplicity == 4:
            return len(self.list[1])