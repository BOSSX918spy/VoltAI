import math

c = 3e8


def wavelength(freq):
    return c / freq


def friis_tx_power(pt, gt, gr, wavelength, distance):
    return pt * gt * gr * (wavelength / (4 * math.pi * distance))**2