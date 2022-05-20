import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def SIR_model(x, t):
    alpha = 0.3
    beta = 0.01

    S = x[0]
    I = x[1]
    R = x[2]

    dS_dt = -beta*S*I + 0.01 * R
    dI_dt = beta*S*I-alpha*I + 0.01 * R
    dR_dt = alpha*I - 0.02 * R

    return [dS_dt, dI_dt, dR_dt]


# Anfangsbedingungen
S0 = 200
I0 = 1
R0 = 0

x0 = [S0, I0, R0]

# Zeitschritte
t = np.linspace(0, 60, 501)

# Das DGE lösen
x = odeint(SIR_model, x0, t)  # Numerisches Iterationsverfahren

S = x[:, 0]
I = x[:, 1]
R = x[:, 2]

# Grafik erstellen
fig, ax = plt.subplots()
ax.set_title("Modifiziertes SIR Modell mit \u03B3: 0.2", size=25)
ax.plot(t, S, label="S")
ax.plot(t, I, label="I")
ax.plot(t, R, label="R")

ax.tick_params(labelsize=22)
ax.set_xlabel('Zeit', size=22)
ax.set_ylabel('Bevölkerung', size=22)
ax.grid()
ax.legend(fontsize=22)
plt.show()
