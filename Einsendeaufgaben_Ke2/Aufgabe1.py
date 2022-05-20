"""
Aufgabe 1
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameter
C = 0.2

y_0 = 20
y_20 = 200
START_TIME = 0
END_TIME = 20



def get_dydt(c, y):
    return c * y


def explicit_euler_method(simulation_steps):
    y = y_0
    y_list = [y_0]
    timesteps = np.linspace(START_TIME, END_TIME, simulation_steps)
    delta_t = (END_TIME - START_TIME) / simulation_steps
    for time in range(simulation_steps-1):
        dydt = get_dydt(C, y)
        y += delta_t * dydt
        y_list.append(y)
    return timesteps, y_list


def implicit_euler_method(simulation_steps):
    y = y_20
    y_list = [y_20]
    timesteps = np.linspace(END_TIME, 0, simulation_steps)
    delta_t = (END_TIME - START_TIME) / simulation_steps
    for i in range(simulation_steps-1):
        dydt = get_dydt(C, y)
        y -= delta_t * dydt
        y_list.append(y)
    return timesteps, y_list


if __name__ == '__main__':
    timesteps_implicit_5, y_list_implicit_5 = implicit_euler_method(5)
    timesteps_implicit_10, y_list_implicit_10 = implicit_euler_method(10)
    timesteps_implicit_25, y_list_implicit_25 = implicit_euler_method(25)
    timesteps_implicit_50, y_list_implicit_50 = implicit_euler_method(50)
    timesteps_implicit_100, y_list_implicit_100 = implicit_euler_method(100)
    timesteps_implicit_250, y_list_implicit_250 = implicit_euler_method(200)

    timesteps_explicit_5, y_list_explicit_5 = explicit_euler_method(5)
    timesteps_explicit_10, y_list_explicit_10 = explicit_euler_method(10)
    timesteps_explicit_25, y_list_explicit_25 = explicit_euler_method(25)
    timesteps_explicit_50, y_list_explicit_50 = explicit_euler_method(50)
    timesteps_explicit_100, y_list_explicit_100 = explicit_euler_method(100)
    timesteps_explicit_250, y_list_explicit_250 = explicit_euler_method(200)

    # Plotten
    fig = plt.figure()

    ax1 = fig.add_subplot(121)  # Erstellen vom ersten Subplots
    ax1.set_title("Implezites Eulerverfahren mit c= {}".format(C), size=25)  # Erstellen vom Titel
    ax1.plot(timesteps_implicit_5, y_list_implicit_5, label="Zeitschritte: 5")
    ax1.plot(timesteps_implicit_10, y_list_implicit_10, label="Zeitschritte: 10")
    ax1.plot(timesteps_implicit_25, y_list_implicit_25, label="Zeitschritte: 25")
    ax1.plot(timesteps_implicit_50, y_list_implicit_50, label="Zeitschritte: 50")
    ax1.plot(timesteps_implicit_100, y_list_implicit_100, label="Zeitschritte: 100")
    ax1.plot(timesteps_implicit_250, y_list_implicit_250, label="Zeitschritte: 200")
    ax1.set_xlabel("Ort ", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax1.set_ylabel("Population", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.legend(fontsize=20)
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid()


    # 2. Diagramm
    ax2 = fig.add_subplot(122)  # Erstellen vom zweiten Subplott
    ax2.set_title("Explezites Eulerverfahren mit c = {}".format(C), size=25)
    ax2.plot(timesteps_explicit_5, y_list_explicit_5, label="Zeitschritte: 5")
    ax2.plot(timesteps_explicit_10, y_list_explicit_10, label="Zeitschritte: 10")
    ax2.plot(timesteps_explicit_25, y_list_explicit_25, label="Zeitschritte: 25")
    ax2.plot(timesteps_explicit_50, y_list_explicit_50, label="Zeitschritte: 50")
    ax2.plot(timesteps_explicit_100, y_list_explicit_100, label="Zeitschritte: 100")
    ax2.plot(timesteps_explicit_250, y_list_explicit_250, label="Zeitschritte: 200")
    ax2.set_xlabel("Ort", size=22, labelpad=20)
    ax2.set_ylabel("Population", size=22, labelpad=20)
    ax2.tick_params(labelsize=20)
    ax2.legend(fontsize=20)
    ax2.grid()
    #ax2.invert_xaxis()

    plt.show()
