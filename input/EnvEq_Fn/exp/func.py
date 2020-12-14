import numpy as np

def f_res(res):
    if res<0:
        return 0
    else:
        return 1-np.exp(-res)
