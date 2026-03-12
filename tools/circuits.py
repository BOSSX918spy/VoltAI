import math

def voltage_divider(vin, r1, r2):
    return vin * (r2 / (r1 + r2))

def ohms_law(v=None, i=None, r=None):

    if v is None:
        return i * r

    if i is None:
        return v / r

    if r is None:
        return v / i

def rc_cutoff(r, c):
    return 1 / (2 * math.pi * r * c)