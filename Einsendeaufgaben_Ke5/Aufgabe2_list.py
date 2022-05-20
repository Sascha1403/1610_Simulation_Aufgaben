import numpy as np
import matplotlib.pyplot as plt
import time
from typing import Tuple



def read_data() -> Tuple[list, list, list, list]:
    """Einlesen des Textfiles huetten.txt"""


    file = open("huetten.txt", 'r')
    f = file.readlines()
    names = []
    x_coords = []
    y_coords = []
    altitude = []

    for i, line in enumerate(f):
        data = line.split()
        names.append(data[0])
        x_coords.append(float(data[1]))
        y_coords.append(float(data[2]))
        altitude.append(float(data[3]))

    return names, x_coords, y_coords, altitude


def get_distance(x1: int, x2: int, y1: int, y2: int) -> int:
    """Berechnen der Distance zwischen den Hütten"""
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_neighbour_hood(x_coords: list, y_coords:list) -> list:
    """ Erstellen einer Liste mit allen Nachbarschaftsbeziehungen """

    # Iterieren über alle Hütten
    neighbour_hood = []
    r_cut = 2
    for i in range(len(x_coords)):

        # Erstellen einer Liste aller benachbarten Hütten von i
        neighbours = []
        for j in range(len(x_coords)):
            if i == j: continue
            if i == 5 and j == 12:
                print(x_coords[i], x_coords[j], y_coords[i], y_coords[j])
            r_ij = get_distance(x_coords[i], x_coords[j], y_coords[i], y_coords[j])
            if r_cut > r_ij:
                neighbours.append(j)

        # Benachbarte Hütten von i der Gesamtliste aller benachbarten Hütten anfügen
        neighbour_hood.append(neighbours)
    return neighbour_hood

def get_altitude_from_neighbour_hood(neighbour_hood: list, altidude: list) -> list:
    ''' Erstellen einer Liste des Höhenunterschieds für alle benachbarten Hütten'''

    # Iterieren über alle Hütten
    neighbour_hood_altidude = []
    for i in range(len(neighbour_hood)):

        # Berechnen des Höhenunterschied aller benachbarter Hütten von i
        neighbours_altidude = []
        for j in range(len(neighbour_hood[i])):
            index_hut_j = neighbour_hood[i][j][0]
            altidude_differce = abs(altidude[i] - altidude[index_hut_j])
            neighbours_altidude.append((index_hut_j, altidude_differce))

        # Benachbarte Hütten von i der Gesamtliste alle benachbarter Hütten anfügen
        neighbour_hood_altidude.append(neighbours_altidude)
    return neighbour_hood_altidude


def get_neighbour_hood_altidude(x_coords: list, y_coords:list, altidude:list) -> list:
    ''' Berechnen des Höhenunterschieds für alle benachbarten Hütten'''

    # Iterieren über alle Hütten
    neighbour_hood_altidude = []
    r_cut = 2
    for i in range(len(x_coords)):

        # Ermitteln des Abstand zwischen den Hütten und bei benachbarten Hütten Höhenunterschied ermitteln
        neighbours_altidude = []  # Gesamtliste aller benachbarten Hütten
        for j in range(len(x_coords)):
            if i == j: continue
            r_ij = get_distance(x_coords[i], x_coords[j], y_coords[i], y_coords[j])

            # Bei benachbarter Hütte von i Höhenunterschied berechnen und Liste von i anfügen
            if r_cut > r_ij:
                altidude_differce = abs(altidude[i]-altidude[j])
                neighbours_altidude.append((j, altidude_differce))

        # Liste der benachbarten Hütten von i Gesamtliste anfügen
        neighbour_hood_altidude.append(neighbours_altidude)

    return neighbour_hood_altidude

def create_huts_card(names, x_coords, y_coords, neighbour_hood):
    """ Plotten der Karte aller benachbarten Hütten """
    fig, ax = plt.subplots()
    ax.set_title("Berghütten des Mangfallgebirges", size=25)
    ax.plot(x_coords, y_coords, 'bo')
    ax.grid(which='major', linestyle='-', linewidth='0.75', color='black')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax.minorticks_on()
    ax.set_ylim(0,12)
    ax.set_xlim(0,12)
    ax.tick_params(labelsize=22)
    ax.set_xlabel('X-Koordinaten', size=22)
    ax.set_ylabel('Y-Koordinaten', size=22)
    ax.set_aspect('equal', adjustable='box')

    for i in range (len(names)):
        ax.text(x_coords[i]+0.125,y_coords[i]-0.25,names[i])

    for i in range (len(neighbour_hood)):
        for j in range(len(neighbour_hood[i])):
            index_near_house = neighbour_hood[i][j]
            ax.plot([x_coords[i], x_coords[index_near_house]], [y_coords[i], y_coords[index_near_house]], 'b')

    plt.show()




if __name__ == '__main__':
    names,  x_coords, y_coords, altitude = read_data()
    neighbour_hood = get_neighbour_hood(x_coords, y_coords)

    start_proc = time.process_time()
    neighbour_hood = get_neighbour_hood(x_coords, y_coords)
    for i in range(1000):
        neighbour_hood = get_altitude_from_neighbour_hood(neighbour_hood, altitude)
    ende_proc = time.process_time()
    print('Systemzeit: {:5.3f}s\n'.format(ende_proc - start_proc))

    start_proc = time.process_time()
    for i in range(1000):
        neighbour_hood = get_neighbour_hood_altidude(x_coords, y_coords, altitude)
    ende_proc = time.process_time()
    print('Systemzeit: {:5.3f}s'.format(ende_proc - start_proc))


