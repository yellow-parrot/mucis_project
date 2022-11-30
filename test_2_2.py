import random
from random import randint
from .Pers_drum_lib3 import *
from .Pers_sequence3 import *
from .Pers_strum2 import *
from .Pers_random_gen import *
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

chord, multiplicity = Random_Gen()
music(chord, multiplicity)

Clock.every(48, lambda: playing())



Clock.clear()



#p3 >> sinepad(list(P[0,0,8,0,9,0,8,0,-5,-5,3,6,-6,-6,2,3] / 2), dur = 1/2, amp = 2)
