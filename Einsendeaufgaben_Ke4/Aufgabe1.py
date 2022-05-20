import matplotlib.pyplot as plt
import numpy as np


def get_xn1(xn: float, r: float) -> float:
    """ Berechnen der Rhabarbarpflanzen im nächsten Jahr """
    return xn * (4 - xn) - r


def get_xn(n: int, r: float, x0: float) -> list:
    """ Berechnen der Rhabarbarpflanzen über den gesamten Zeitraum """
    xn = [x0]
    for i in range(n - 1):
        xn1 = get_xn1(xn[-1], r)
        xn.append(xn1)
    return xn


def plot_xn_task1(m: int) -> None:
    """ Aufgabe 1.1 """
    r1 = 0.1
    r2 = 1.2
    r3 = 1.7
    x0 = 1

    timeline = [i for i in range(m)]
    population_1 = get_xn(m, r1, x0)
    population_2 = get_xn(m, r2, x0)
    population_3 = get_xn(m, r3, x0)

    population = [population_1, population_2, population_3]
    r = [r1, r2, r3]

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    for i in range(3):
        ax[i].plot(timeline, population[i], label="r: {}".format(r[i]))
        ax[i].set_title("Rhabarberpflanzen", size=25)
        ax[i].tick_params(labelsize=22)
        ax[i].set_xlabel("Jahre", size=22)
        ax[i].set_ylabel("Population", size=22)
        ax[i].legend(loc="lower right",fontsize=20)
        ax[i].grid()
        ax[i].grid(which='major', linestyle='-', linewidth='0.75', color='black')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        ax[i].minorticks_on()

    plt.show()


def get_xaxes_bifurkation_diagramm(r_lowerbound: float, r_upperbound: float, m: int, last: int) -> list:
    """ Erstellen der X-Achse des Bifurkationsdiagramm """
    r_values = np.linspace(r_lowerbound, r_upperbound, m)
    xaxes = [r_values[i] for i in range(m) for j in range(last)]
    return xaxes


def get_yaxes_bifurkation_diagramm(r_lowerbound: float, r_upperbound: float, m: int, n: int, x0: float, last: int) -> list:
    """ Erstellen der Y-Achse (Xn -Werte) für das Bifurkationsdiagramm """
    r_values = np.linspace(r_lowerbound, r_upperbound, m)
    y_axes = get_xn(n, r_lowerbound, x0)[-last:]
    for i in range(1, n):
        y_axes = y_axes + get_xn(n, r_values[i], x0)[-last:]
    return y_axes


def plot_bifurkation_diagramm(r_lowerbound: float, r_upperbound: float, m: int, n: int, x0: float, last: int) -> None:
    """ Plotten vom Bifurkationsdiagramm"""
    x_axes = get_xaxes_bifurkation_diagramm(r_lowerbound, r_upperbound, m, last)
    y_axes = get_yaxes_bifurkation_diagramm(r_lowerbound, r_upperbound, m, n, x0, last)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Bifurkationsdiagramm", size=25)  # Erstellen vom Titel
    ax1.plot(x_axes, y_axes, ',k', alpha=.5)
    ax1.set_xlabel("Erntemenge r", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax1.set_ylabel("Dutzende Rhabarberpflanzen x", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid()
    ax1.grid(which='major', linestyle='-', linewidth='0.75', color='black')
    ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax1.minorticks_on()
    plt.show()

plot_xn_task1(30)
plot_bifurkation_diagramm(0, 2, 1000, 1000, 100, 1)
