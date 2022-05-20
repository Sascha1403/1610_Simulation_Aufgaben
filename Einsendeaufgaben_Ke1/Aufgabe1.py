import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import sin, cos

''' 2.1 Bahnkurve des Trainers '''


def model(y, t):  # y zwei Dim Vektor
    dxdt = -5 * sin(t)  # Geschwindigkeit in x-Richtung
    dydt = 5 * cos(t)  # Geschwindigkeit in y-Richtung
    return [dxdt, dydt]


# Anfangsbedingungen
x0 = 5
y0 = 0
InitialConditions = [x0, y0]

# Zeitschritte
t = np.linspace(0, 60, 501)

# Das DGE lösen
heart = odeint(model, InitialConditions, t)  # Numerisches Iterationsverfahren

# Grafik erstellen
plt.plot(heart[:, 0], heart[:, 1])
plt.xlabel('x-Richtung')
plt.ylabel('y-Richtung')
plt.axis('square')
plt.grid()
plt.show()

''' 2.2 Bahnkurve des Blindenhundes '''


def model_dog(x, t):
    position_trainer = np.array([x[0], x[1]])
    postion_dog = np.array([x[2], x[3]])

    dxdt_trainer = -5 * sin(t)  # Geschwindigkeit in x-Richtung
    dydt_trainer = 5 * cos(t)  # Geschwindigkeit in y-Richtung
    v_trainer = (dxdt_trainer, dydt_trainer)

    leash = position_trainer - postion_dog
    v_dog = np.dot(v_trainer, leash) / np.dot(leash, leash) * leash
    dxdt_dog = v_dog[0]
    dydt_dog = v_dog[1]

    return [dxdt_trainer, dydt_trainer, dxdt_dog, dydt_dog]


# Anfangsbedingungen
x0_trainer = 5
y0_trainer = 0
x0_dog = 10
y0_dog = 0
initial_conditions = [x0_trainer, y0_trainer, x0_dog, y0_dog]

# Zeitschritte
t = np.linspace(0, 60, 501)

# Das DGE lösen
Positions = odeint(model_dog, initial_conditions, t)  # Numerisches Iterationsverfahren

# Grafik erstellen
plt.plot(Positions[:, 2], Positions[:, 3])
plt.xlabel('x-Richtung')
plt.ylabel('y-Richtung')
plt.axis('square')
plt.grid()
plt.show()
