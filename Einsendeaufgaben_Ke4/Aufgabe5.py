import matplotlib.pyplot as plt


def euler(t, n, x0, y0):
    xn = [x0]
    yn = [y0]
    delta_t = t / n
    for i in range(n - 1):
        derivative_dx = 1.1 * xn[-1] - 0.4 * xn[-1] * yn[-1]
        xn_i1 = xn[-1] + derivative_dx * delta_t

        derivative_dy = 0.1 * xn[-1] * yn[-1] - 0.4 * yn[-1]
        yn_i1 = yn[-1] + derivative_dy * delta_t

        xn.append(xn_i1)
        yn.append(yn_i1)
    return xn, yn


def plot_euler(t, n, x0, y0):
    xn, yn = euler(t, n, x0, y0)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("x-y-Diagramm", size=25)  # Erstellen vom Titel
    ax1.scatter(xn, yn, s=1, c='green')
    ax1.set_xlabel("Population Regenwürmer", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
    ax1.set_ylabel("Population Vögel", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
    ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
    ax1.grid()
    plt.show()


def plot_euler_task1(t, n):
    x0 = 10
    y0 = [2, 6, 8, 10]

    fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False)
    fig.suptitle('X-Y Diagramm', fontsize="24")

    for i in range(2):
        xn, yn = euler(t, n, x0, y0[i])
        ax[0][i].plot(xn, yn, label="x0: 10, y0: {}".format(y0[i]))
        ax[0][i].tick_params(labelsize=22)
        ax[0][i].set_xlabel("Regenwürmer", size=22)
        ax[0][i].set_ylabel("Vögel", size=22)
        ax[0][i].legend(loc="lower right", fontsize=18)
        ax[0][i].grid(which='major', linestyle='-', linewidth='0.75', color='black')
        ax[0][i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        ax[0][i].minorticks_on()

    for j in range(2):
        xn, yn = euler(t, n, x0, y0[j + 2])
        ax[1][j].plot(xn, yn, label="x0: 10, y0: {}".format(y0[j + 2]))
        ax[1][j].tick_params(labelsize=22)
        ax[1][j].set_xlabel("Regenwürmer", size=22)
        ax[1][j].set_ylabel("Vögel", size=22)
        ax[1][j].legend(loc="lower right", fontsize=18)
        ax[1][j].grid(which='major', linestyle='-', linewidth='0.75', color='black')
        ax[1][j].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        ax[1][j].minorticks_on()

    plt.show()


plot_euler_task1(30, 30000)
plot_euler(30, 30000, 10, 5)
