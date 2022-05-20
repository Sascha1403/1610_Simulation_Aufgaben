import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

def read_data():
    file = open("huetten.txt", 'r')
    f = file.readlines()
    data = np.empty(shape=(26, 4), dtype=object)
    for i, line in enumerate(f):
        data[i] = line.split()

    headline = ("Name", "X-Koordinate", "Y-Koordinate", "Höhenmeter")
    huts = pd.DataFrame(data, columns=headline)
    huts["X-Koordinate"] = pd.to_numeric(huts["X-Koordinate"])
    huts["Y-Koordinate"] = pd.to_numeric(huts["Y-Koordinate"])
    huts["Höhenmeter"] = pd.to_numeric(huts["Höhenmeter"])
    return huts


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def letter_to_int(letter):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alphabet.index(letter)


def get_neighbour_hood(huts):
    neighbour_hood = np.full([26], None)
    r_cut = 2
    for i in range(huts.shape[0]):
        neighbour_hood_hut = []
        for j in range(huts.shape[0]):
            if i == j: continue
            r_ij = get_distance(huts.iat[i, 1], huts.iat[j, 1], huts.iat[i, 2], huts.iat[j, 2])
            if r_cut > r_ij:
                neighbour_hood_hut.append(huts.iat[j, 0])
        neighbour_hood[i] = neighbour_hood_hut
    return neighbour_hood

def get_altitude_differce(neighbour_hood):
    neighbour_hood_altidude = np.zeros((26, 26))
    for i in range(len(neighbour_hood)):
        altidude_hut_1 = huts.at[i, "Höhenmeter"]
        for j in range(len(neighbour_hood[i])):
            near_hut = neighbour_hood[i][j]
            index_hut = letter_to_int(near_hut)
            altidude_hut_2 = huts.at[index_hut, "Höhenmeter"]

            altitude_differce = abs(altidude_hut_1 - altidude_hut_2)
            neighbour_hood_altidude[i][index_hut] = altitude_differce

    return neighbour_hood_altidude


def get_neighbour_hood_and_altitude_differce(huts):
    neighbour_hood_altidude = np.zeros((26, 26))
    r_cut = 2
    for i in range(huts.shape[0]):
        for j in range(huts.shape[0]):
            if i == j: continue
            r_ij = get_distance(huts.iat[i, 1], huts.iat[j, 1], huts.iat[i, 2], huts.iat[j, 2])
            if r_cut > r_ij:
                altitude_differce = abs(huts.iat[j, 3] - huts.iat[i, 3])
                neighbour_hood_altidude[i][j] = altitude_differce
    return neighbour_hood_altidude



if __name__ == '__main__':
    huts = read_data()

    start_proc = time.process_time()
    neighbour_hood = get_neighbour_hood(huts)
    for i in range(1000):
        neighbour_hood = get_altitude_differce(neighbour_hood)
    ende_proc = time.process_time()
    print('Systemzeit: {:5.3f}s\n'.format(ende_proc - start_proc))

    start_proc = time.process_time()
    for i in range(1000):
        neighbour_hood = get_neighbour_hood_and_altitude_differce(huts)
    ende_proc = time.process_time()
    print('Systemzeit: {:5.3f}s'.format(ende_proc - start_proc))


