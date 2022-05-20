import numpy as np
import matplotlib.pyplot as plt

x_axis = np.linspace(0, 20, 100)
t_axis = np.linspace(0, 10, 100)
A = 6
d = 6
omega = 2
kappa = 0.3

def get_density(x, t):
    return A * np.cos(omega * t + kappa * x) + d


def get_density_with_reflexion(x, t):
    return A * np.cos(kappa * x) * np.sin(omega * t) + d


def simulation(time):
    density = []
    for x in x_axis:
        desity_x = get_density(x, time)
        density.append(desity_x)
    return density

def simulation_wall_reflexion(time):
    density = []
    for x in x_axis:
        desity_x = get_density_with_reflexion(x, time)
        density.append(desity_x)
    return density

def simulation_ort(ort):
    density = []
    for t in t_axis:
        desity_x = get_density(ort, t)
        density.append(desity_x)
    return density


if __name__ == '__main__':
    density_0 = simulation(0)
    density_4 = simulation(4)
    density_8 = simulation(8)

    density_wall_reflexion_0 = simulation_wall_reflexion(0)
    density_wall_reflexion_4 = simulation_wall_reflexion(4)
    density_wall_reflexion_8 = simulation_wall_reflexion(8)

    density_ort_0 = simulation_ort(0)
    density_ort_4 = simulation_ort(4)
    density_ort_8 = simulation_ort(8)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.set_title("Dichtefunktionen ohne Berücksichtigung", size=25)  # Erstellen vom Titel
    ax1.plot(x_axis, density_0, label="t=0")
    ax1.plot(x_axis, density_4, label="t=4")
    ax1.plot(x_axis, density_8, label="t=8")
    ax1.set_ylabel("Population", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.legend(loc="upper left", fontsize=20)
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid()

    ax2 = fig.add_subplot(212)
    ax2.set_title("Dichtefunktionen mit Berücksichtigung der Randreflexion", size=25)  # Erstellen vom Titel
    ax2.plot(x_axis, density_wall_reflexion_0, label="t=0")
    ax2.plot(x_axis, density_wall_reflexion_4, label="t=4")
    ax2.plot(x_axis, density_wall_reflexion_8, label="t=8")
    ax2.set_xlabel("Ort", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax2.set_ylabel("Population", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax2.legend(loc= "upper left", fontsize=20)
    ax2.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax2.grid()
    plt.show()

