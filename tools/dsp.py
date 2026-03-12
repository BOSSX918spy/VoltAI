import numpy as np


def nyquist_frequency(fs):
    return fs / 2


def alias_frequency(signal_freq, sampling_rate):
    return abs(signal_freq - sampling_rate)


def fft_spectrum(signal):
    return np.fft.fft(signal).tolist()