import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def SIR_model(x, t):
    r = 2
    K = 0.02

    dx_dt = r * x[0] * (1 - x[0]/K)

    return [dx_dt]


# Anfangsbedingungen
S0 = 200
I0 = 1
R0 = 0

x0 = [1]

# Zeitschritte
t = np.linspace(0, 10, 501)

# Das DGE lösen
x = odeint(SIR_model, x0, t)  # Numerisches Iterationsverfahren

S = x[:, 0]

# Grafik erstellen
fig, ax = plt.subplots()
ax.set_title("Modifiziertes SIR Modell mit \u03B3: 0.2", size=25)
ax.plot(t, S, label="S")


ax.tick_params(labelsize=22)
ax.set_xlabel('Zeit', size=22)
ax.set_ylabel('Bevölkerung', size=22)
ax.grid()
ax.legend(fontsize=22)
plt.show()
