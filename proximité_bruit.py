import random

def proximite_bruit(self,arene):
    MAX = 6.0
    MIN = 1.0
    bruit = random.randrange(MIN,MAX,0.1)
    res = arene.proximite()*bruit
    return res

