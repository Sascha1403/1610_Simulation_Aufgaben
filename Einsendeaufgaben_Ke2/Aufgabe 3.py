import numpy as np
from matplotlib import pyplot as plt
import matplotlib.axes._axes as axes
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.figure as figure
import matplotlib as mpl


class CalculateDensity:
    """ A class used to calculate the Density """

    def __init__(self, lenght_pool=20, number_parts_pool=200, experiment_time = 270, timesteps=360, p_max=1,
                 v_max=0.1):
        self.l = lenght_pool
        self.m = number_parts_pool
        self.t = experiment_time
        self.n = timesteps
        self.rho_max = p_max
        self.v_max = v_max

    @property
    def delta_t(self):
        return self.t / self.n

    @property
    def h(self):
        return self.l / self.m

    @property
    def time(self):
        return np.linspace(0, self.t, self.n)

    @property
    def pool_parts(self):
        factor_length = (self.m + self.n) / self.m
        return np.linspace(0, self.l * factor_length, self.m + self.n)

    def get_initial_conditions(self):
        """ Return an Array with the initial conditions with the length of the number_parts_pool + timesteps
            because we need p_i+1,j to calculate p_i,j+1 """
        return 0.5 * np.cos(self.pool_parts) + 0.5

    def get_boundary_condition(self):
        """ Return an Array boundary conditions (Value for the density on the time t_0 at the all location x)"""
        return 0.5 * np.cos(self.time) + 0.5

    def initial_density_array(self):
        """The function initialise the initial and boundary condition as an array rho"""
        rho = np.zeros((self.m + self.n, self.n))
        rho[:, 0] = self.get_initial_conditions()
        rho[0, :] = self.get_boundary_condition()
        return rho

    def euler_step(self, rho, i, j):
        rho_i_j1 = rho[i, j] - ((self.delta_t / self.h) * self.v_max) * \
                   ((1 - rho[i + 1, j] / self.rho_max) * rho[i + 1, j] - (1 - rho[i, j] / self.rho_max) * rho[i, j])
        return rho_i_j1

    def mac_cormack(self, rho, i, j):
        def get_f(i, j):
            get_v_i_j = lambda i, j: self.v_max * (1 - (rho[i, j] / self.rho_max))
            return rho[i, j] * get_v_i_j(i, j)

        def get_f_snake(i, j):
            get_v_i_j = lambda i, j: self.v_max * (1 - (rho[i, j] / self.rho_max))
            get_v_snake = lambda rho_snake: self.v_max * (1 - (rho_snake / self.rho_max))
            get_f_i_j = lambda i, j: rho[i, j] * get_v_i_j(i, j)
            get_rho_snake_i_j1 = lambda i, j: \
                rho[i, j] - self.delta_t * (get_f_i_j(i, j) - get_f_i_j(i - 1, j)) / self.h

            f_snake_i_j1 = get_rho_snake_i_j1(i, j) * get_v_snake(get_rho_snake_i_j1(i, j))

            return f_snake_i_j1

        f_snake_i_j1 = get_f_snake(i, j)
        f_snake_i1_j1 = get_f_snake(i+1, j)

        f_i_j = get_f(i, j)
        f_1i_j = get_f(i-1, j)

        rho_i_j1 = rho[i, j] - self.delta_t / 2 * ((f_i_j - f_1i_j) / self.h + (f_snake_i1_j1 - f_snake_i_j1) / self.h)

        return rho_i_j1

    def calculate_rho_euler(self, rho):
        for j in range(self.n - 1):
            for i in range(1, self.n + self.m - j - 1):
                rho_i_j1 = self.euler_step(rho, i, j)
                rho[i, j + 1] = rho_i_j1
        return rho

    def calculate_rho_maccormack(self, rho):
        for j in range(self.n - 1):
            for i in range(1, self.n + self.m - j - 1):
                rho_i_j1 = self.mac_cormack(rho, i, j)
                rho[i, j + 1] = rho_i_j1
        return rho

    def plot_3d(self, rho):
        result = rho[:self.m].T
        x = self.pool_parts[:self.m]
        y = self.time

        xx, yy = np.meshgrid(x, y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        surf =ax.plot_surface(xx, yy, result, linewidth=0)
        surf._facecolors2d = surf._facecolors3d  # Um Titel ploten zu können
        surf._edgecolors2d = surf._edgecolors3d  # Um Titel ploten zu können


        # plt.plot(result.T)
        ax.set_title("MacCormack Verfahren", size = 25)
        ax.set_xlabel('Ortsabschnitte in m', size = 22, labelpad=25)
        ax.set_ylabel('Zeit in sec', size = 22, labelpad=25)
        ax.set_zlabel(r'Dichte $\rho$', size= 22, labelpad=25)
        ax.tick_params(labelsize=20)
        #ax.legend(fontsize=20)
        plt.show()

    def plot_location_2d(self, rho):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)  # Erstellen vom ersten Subplots
        ax1.set_title("MacCormack Verfahren", size=25)  # Erstellen vom Titel
        ax1.plot(self.time, rho[0, :], label="Ortsabschnitt: 0")
        ax1.plot(self.time, rho[50, :], label="Ortsabschnitt: 50")
        ax1.plot(self.time, rho[100, :], label="Ortsabschnitt: 100")
        ax1.plot(self.time, rho[150, :], label="Ortsabschnitt: 150")
        ax1.plot(self.time, rho[199, :], label="Ortsabschnitt: 199")


        ax1.set_xlabel('Zeitschritte $n$', size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
        ax1.set_ylabel(r'Dichte $\rho$', size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
        ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
        ax1.grid()
        ax1.legend(fontsize=20)
        plt.show()

    def plot_time_2d(self, rho, timestep):
        result = rho[:self.m]
        fig = plt.figure()
        ax1 = fig.add_subplot(111)  # Erstellen vom ersten Subplots
        ax1.set_title("MacCormack Verfahren mit einer Simulationszeit von {} sec".format(self.t), size=25)  # Erstellen vom Titel
        ax1.plot(self.pool_parts[:200], result[:,timestep], label="Zeitschritt = {}".format(timestep),
                 linestyle='--', marker='o')


        ax1.set_xlabel('Ortsabschitte $m$', size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
        ax1.set_ylabel(r'Dichte $\rho$', size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
        ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
        ax1.legend(fontsize=20, loc="upper right")
        ax1.grid()
        plt.show()


if __name__ == '__main__':
    ClsCalculateDensity = CalculateDensity()
    int_rho = ClsCalculateDensity.initial_density_array()
    rho_mac = ClsCalculateDensity.calculate_rho_maccormack(int_rho)

    ClsCalculateDensity.plot_3d(rho_mac)
    ClsCalculateDensity.plot_time_2d(rho_mac, 359)
