import numpy as np


def first_order_step_response(K, tau, t):
    return K * (1 - np.exp(-t/tau))


def damping_ratio(zeta):
    if zeta < 1:
        return "Underdamped"
    if zeta == 1:
        return "Critically damped"
    return "Overdamped"