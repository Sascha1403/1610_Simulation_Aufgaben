import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple


def euler(t: int, n: int, x0: float, y0: float, alpha: float, beta: float, gamma: float, rho: float) -> Tuple[list, list]:
    """ Euler Verfahren """
    xn = [x0]
    yn = [y0]
    delta_t = t / n
    for i in range(n-1):
        derivative_dx = -alpha * xn[-1] + beta * xn[-1] * yn[-1]
        xn_i1 = xn[-1] + derivative_dx * delta_t

        derivative_dy = -gamma * yn[-1] + rho * xn[-1] * yn[-1]
        yn_i1 = yn[-1] + derivative_dy * delta_t

        xn.append(xn_i1)
        yn.append(yn_i1)
    return xn, yn


def plot_euler(t: int, n: int, x0: float, y0: float, alpha: float, beta: float, gamma: float, rho: float) -> None:
    c = [2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95]


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("x-y-Diagramm", size=25)  # Erstellen vom Titel

    for i in range(7):
        xn, yn = euler(t, n, c[i], y0, alpha, beta, gamma, rho)
        ax1.plot(xn, yn, label="x0: {}, y0: 8".format(c[i]))
        xn, yn = euler(t, n, x0, c[i], alpha, beta, gamma, rho)
        ax1.plot(xn, yn, label="x0: 8, y0: {}".format(c[i]))


    ax1.set_xlabel("Population Männchen x", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax1.set_ylabel("Population Weibchen y", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid()
    ax1.legend(fontsize=22)
    ax1.set_xlim(0, 8)
    ax1.set_ylim(0, 8)
    plt.show()

plot_euler(20, 500, 8, 8, 0.5, 0.1, 0.5, 0.1)