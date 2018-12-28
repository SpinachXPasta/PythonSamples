%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from time import time as TT
from random import choice as ch
import numpy as np

ac = []
tc = []
N = []
st = TT()
for M in range(1,10000): #Outer loop from 1 to 10000
    st1 = TT()
    score = []a
    runs = 0
    cards = [1,2,3]
    for K in range(1,M): # sub loop that simulates 1 to M(outerloop) games
        aset = []
        host = cards.copy()
        hbk = ch(host) #Randomly choose as answer which host knows
        aset.append(hbk)
        #print("The host knows the answer",hbk)
        player = cards.copy()
        px = ch(player) # Contestanrs random guess
        aset.append(px)
        #print ("Players first choice",px)
        chance = 0
        for i in host: # The computation....host will eliminate P(X|DOOR) = 0
            if i not in aset:
                chance = i
        #print ("The elimination",chance)
        #print (player)
        player.pop(player.index(chance))
        player.pop(player.index(px))
        #print ("final answe",player)
        if player[0] == hbk:
            score.append(1)
        else:
            score.append(0)
        runs = K
        #print ("\n\n")
    ac.append(np.mean(score))
    N.append(M)
    en1 = TT()
    tc.append(en1-st1)
en = TT()
print ("Total time for Loop  ", en - st )

plt.plot(N,ac)
plt.show()

plt.plot(N,tc)
plt.show()

print ("Averge Wins",np.mean(ac))
