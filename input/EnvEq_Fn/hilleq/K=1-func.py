import numpy as np

def f_res(res):
    if res<0:
        return 0
    else:
        return res/(1+res)