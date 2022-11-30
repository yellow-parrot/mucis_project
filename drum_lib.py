from FoxDot import *
class Drum_func:
#
    def mute(self):
        p4.stop()
#
#   
class Drum4(Drum_func):
    def play4(self, chord, n):
        if n == 0:
            p4 >> play("-x-oxx-o", amp = 0.6)
        if n == 1:
            p4 >> play("x-o-", amp = P[1, 1, 1, 1,] * 0.6)
        if n == 2:
            p4 >> play("<[- - ][# ]>< (xo)>", amp = 0.4)
        if n == 3:
            p4 >> play("x--o(- )", amp = 1 * 0.6)
#
    def number4(self):
        return 4
#
class Drum3(Drum_func):
    def play3(self, chord, n):
        if n == 0:
            p4 >> play("x--o--", amp = P[1, 1, 1] * 0.6)
        if n == 1:
            p4 >> play("x- o- ", amp = P[1, 1, 0] * 0.6)
        if n == 2:
            p4 >> play("ox-o-x", amp = 0.6)
#
    def number3(self):
        return 3
#
class Drum(Drum3, Drum4):
    def play(self, even, chord, n):
        if even == 3:
            self.play3(chord, n)
        if even == 4:
            self.play4(chord, n)
#
    def number(self, multiplicity):
        if multiplicity == 3:
            return self.number3()
        if multiplicity == 4:
            return self.number4()
#drum = Drum()
#
#chord, multiplicity = Random_Gen()
#
#print(drum.number(multiplicity))
#
#drum.play(multiplicity, chord, 2)
#
#drum.mute()
#
#__________________________________________________________________________________________
#
