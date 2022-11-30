from FoxDot import *
class Strum_func:
#
    def mute(self):
        p1.stop()
#
    def chordlist(self, chord, repeats):
        ch = []
        for i in range(len(chord)):
            ch += [chord[i]] * repeats
        return(ch)
#       
class Strum4(Strum_func):
#
    def play4(self, chord, n):
        if n == 0:
            p1 >> pluck( list(P(self.chordlist(chord, 2) ) - 7 ), dur = 1, amp = P[0.5, 0.5, 0.7, 0.5] * 1)
        if n == 1:
            p1 >> pluck(list(P(self.chordlist(chord, 4)) - 7), dur = P[1.5, 0.5, 0.5, 0.5] * 1, amp = 1)
        if n == 2:
            p1 >> pluck(list(P(self.chordlist(chord, 1)) - 7), dur = 1, amp = P[0.7, 0.5, 0.5] * 1)
#
    def number4(self):#количесвто функций с повторяемостью кратной 4
        return 3    
#
#
class Strum3(Strum_func):   
# 
    def play3(self, chord, n):
        if n == 0:
            p1 >> pluck(list(P(self.chordlist(chord, 6)) - 7), dur = P[0.5, 1.5, 0.5, 0.5, 0.5, 0.5] * 1, amp = 0.5)
        if n == 1:
            p1 >> pluck(list(P(self.chordlist(chord, 9)) - 7), dur = P[1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 1] * 1, amp = 0.8)
        if n == 2:
            p1 >> pluck(list(P(self.chordlist(chord, 1)) - 7), dur = 1, amp = P[0.7, 0.5, 0.5] * 3)
#
    def number3(self):
        return 3
#
class Strum(Strum4, Strum3):
#
    def play(self, multiplicity, chord, n):
        if multiplicity == 3:
            self.play3(chord, n)
        if multiplicity == 4:
            self.play4(chord, n)
#
    def number(self, multiplicity):
        if multiplicity == 3:
            return self.number3()
        if multiplicity == 4:
            return self.number4()