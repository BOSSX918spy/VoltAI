import numpy as np


def convolution(x, h):
    return np.convolve(x, h).tolist()


def system_stability(poles):
    for p in poles:
        if p >= 0:
            return "System is unstable"
    return "System is stable"