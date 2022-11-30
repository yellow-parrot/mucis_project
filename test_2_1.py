import random
from random import randint
from .sequence3 import *
from .drum_lib3 import *
from .strum2 import *
#__________________________________________________________________________ 
def maj1 (a): 
    return (a, a+4, a+7)
def min1 (a): 
    return (a, a+3, a+7)
def ch(m, a):
    if m == 0:
        return maj1(a)
    else:
        return min1(a)
#__________________________________________________________________________
def Random_Gen():
#______________ 
	ch0ton = randint(0,1)
	ch0 = randint(0, 11)
	multiplicity_of_bit = randint(3, 4)
	chlist1 = [[ch0, ch0 + 7, ch0 + 5], [ch0 - 3, ch0 + 2, ch0 + 4]]
	chlist2 = [[ch0 + 7, ch0 + 5], [ch0 - 3, ch0 + 2, ch0 + 4]]
	number_of_chords = [3, 4, 6][randint(0,2)]
#______________
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
