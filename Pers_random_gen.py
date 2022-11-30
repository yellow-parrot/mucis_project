from FoxDot import *
import random
from random import *
#
def maj1 (a):
    return (a, a+4, a+7)
def min1 (a):
    return (a, a+3, a+7)
def ch(m, a):
    if m == 0:
        return maj1(a)
    else:
        return min1(a)
#
def Random_Gen():
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