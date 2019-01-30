import numpy as np
#a mettre dans la classe robot
def val_accelerometre():
    MIN = 0
    MAX = 3
    res = [0,1,2]#self.acceleration;
    r= np.random.rand(3)
    res[0] += r[0] * (MAX-MIN) + MIN
    res[1] += r[1] * (MAX-MIN) + MIN
    res[2] += r[2] * (MAX-MIN) + MIN
    return res
