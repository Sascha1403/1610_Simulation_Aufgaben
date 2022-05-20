import numpy as np
import matplotlib.pyplot as plt

# Constance
a = -9.81


def get_x_t1(x, v, h):
    """ Return the position at the next timestep """
    x_t1 = x + v * h + 1 / 2 * a * h ** 2
    return x_t1


def get_v_t1(v, h):
    """ Return the velocity at the next timestep """
    v_t1 = v + 1 / 2 * (a + a) * h
    return v_t1


def velocity_stoermer_verlet_algorithm(x_0=100, t_0=0, t_n=5, n=100):
    h = (t_n - t_0) / n
    t = np.linspace(t_0, t_n, n)
    x = [x_0]
    v = [0]

    for i in range(n - 1):
        x_t1 = get_x_t1(x[-1], v[-1], h)
        if x_t1 < 0: x_t1 = 0
        v_t1 = get_v_t1(v[-1], h)
        x.append(x_t1)
        v.append(v_t1)

    return x, t


def plot_xy_diagramm(x, t):
    # Grafik erstellen
    fig, ax = plt.subplots()
    ax.set_title("XY-Diagramm", size=25)
    ax.plot(t, x)

    ax.tick_params(labelsize=22)
    ax.set_xlabel('Zeit', size=22)
    ax.set_ylabel('Ort', size=22)
    ax.grid()
    plt.show()


if __name__ == '__main__':
    x, t = velocity_stoermer_verlet_algorithm()
    plot_xy_diagramm(x, t)
