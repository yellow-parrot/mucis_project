import random
from random import randint
#
#__________________________________________________________________________ Вспомогательные функции для формирования аккордов
def maj1 (a): 
    return (a, a+4, a+7)
def min1 (a): 
    return (a, a+3, a+7)
def ch(m, a):
    if m == 0:
        return maj1(a)
    else:
        return min1(a)
#__________________________________________________________________________ Функция рандомной генерации последовательности аккордов и чётности бита
#
def Random_Gen():
#______________ Задаём рандомно тональность первого аккорда (мажор/минор), первую нору первого аккорда, кличество нот в аккорде, вспомогательные списки возможных первых нот последующих аккордов и количество аккордов
	ch0ton = randint(0,1)
	ch0 = randint(0, 11)
	multiplicity_of_bit = randint(3, 4)
	chlist1 = [[ch0, ch0 + 7, ch0 + 5], [ch0 - 3, ch0 + 2, ch0 + 4]]
	chlist2 = [[ch0 + 7, ch0 + 5], [ch0 - 3, ch0 + 2, ch0 + 4]]
	number_of_chords = [3, 4, 6][randint(0,2)]
#______________ Рандомно формируем список аккордов
	chord = []
	chord.append(ch(ch0ton, ch0))
#	print(number_of_chords)
	for i in range(number_of_chords - 2):
		ton = randint(0, 1)
		r_ = chlist1[ton][randint(0, 2)]
		while (abs(r_ - chord[i][0]) > 7) or ((r_ - chord[i][0]) == 0):
			r_ = chlist1[ton][randint(0, 2)]
		chord.append(ch(ton, r_))
	ton = randint(0, 1)
	r_ = chlist2[ton][randint(0, len(chlist2[ton])-1)]
	while (abs(r_ - chord[-1][0]) > 7) or ((r_ - chord[-1][0]) == 0):
		r_ = chlist2[ton][randint(0, len(chlist2[ton]) - 1)]
	chord.append(ch(ton, r_))
	print(chord, '\n', multiplicity_of_bit)
	return (chord, multiplicity_of_bit)
#
#__________________________________________________________________________ Класс, вдохновлённый гитарным боем
#
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
#
#
#__________________________________________________________________________________________
#
#
#strum = Strum()
#
#chord, multiplicity = Random_Gen()
#
#print (strum.number(multiplicity))
#
#strum.play(multiplicity, chord, 1)
#
#strum.mute()
#
#
#__________________________________________________________________________________________ Класс нотных последовательностей, сформированных из имеющихся аккордов
#
#
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
#
#
#__________________________________________________________________________________________
#
#sequence = Sequence()
#
#chord, multiplicity = Random_Gen()
#
#print(sequence.number(multiplicity))
#
#sequence.play(multiplicity, chord, 2)
#
#sequence.mute()
#
#__________________________________________________________________________________________ Класс ударных
#
#
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
#
#__________________________________________________________________________________________
#
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
#
strum = Strum()
sequence = Sequence()
drum = Drum()
#
#
def music(chord, multiplicity):
    strum.play(multiplicity, chord, randint(0, strum.number(multiplicity) - 1))
    sequence.play(multiplicity, chord, randint(0, sequence.number(multiplicity) - 1))
    drum.play(multiplicity, chord, randint(0, drum.number(multiplicity) - 1))
#
def mute():
    strum.mute()
    sequence.mute()
    drum.mute()
#
chord, multiplicity = Random_Gen()
#
#__________________________________________________________________________________________
#
#
def playing():
    chord, multiplicity = Random_Gen()
    music(chord, multiplicity)
    Clock.every(12, lambda: music(chord, multiplicity))



Clock.every(48, lambda: playing())



Clock.clear()



#p3 >> sinepad(list(P[0,0,8,0,9,0,8,0,-5,-5,3,6,-6,-6,2,3] / 2), dur = 1/2, amp = 2)
