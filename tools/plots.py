import numpy as np
import matplotlib.pyplot as plt


def rc_bode_plot(r, c):

    f = np.logspace(1, 6, 500)
    w = 2 * np.pi * f

    h = 1 / np.sqrt(1 + (w * r * c)**2)

    plt.figure()
    plt.semilogx(f, 20 * np.log10(h))
    plt.title("RC Low-Pass Frequency Response")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)

    path = "rc_bode.png"
    plt.savefig(path)
    plt.close()

    return path


def first_order_step(K, tau):

    t = np.linspace(0, 5 * tau, 500)
    y = K * (1 - np.exp(-t / tau))

    plt.figure()
    plt.plot(t, y)
    plt.title("First-Order Step Response")
    plt.xlabel("Time")
    plt.ylabel("Output")
    plt.grid(True)

    path = "step_response.png"
    plt.savefig(path)
    plt.close()

    return path