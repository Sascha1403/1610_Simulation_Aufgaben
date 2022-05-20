import matplotlib.pyplot as plt
import numpy as np


def euler(t, n, x0, r, K):
    xn = [x0]
    delta_t = t / n
    for i in range(n-1):
        derivative_dx = r*xn[-1]*(1-xn[-1]/K)
        xn_i1 = xn[-1] + derivative_dx * delta_t
        xn.append(xn_i1)
    return xn


def plot_euler(t, n, x0, r, K):
    xn = euler(t, n, x0, r, K)
    timeline = np.linspace(0, t, n)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Regenwürmer Population", size=25)  # Erstellen vom Titel
    ax1.plot(timeline, xn)
    ax1.set_xlabel("Zeit", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax1.set_ylabel("Population", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid(which='major', linestyle='-', linewidth='0.75', color='black')
    ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax1.minorticks_on()
    ax1.set_ylim(0, 10)
    plt.show()

plot_euler(10, 500, 1, 2, 5)