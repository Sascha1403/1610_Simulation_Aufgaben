import numpy as np
import matplotlib.pyplot as plt
import random as ra

class CheckIn:
    def __init__(self, alpha, mu, simulation_steps):
        self.alpha = alpha
        self.mu = mu
        self.simulation_steps = simulation_steps

        self.time = [0]

        self._distribution_arrival_time = np.array([ra.expovariate(self.alpha) for i in range(self.simulation_steps)])

        self._distribution_processing_time = np.array([ra.expovariate(self.mu) for i in range(self.simulation_steps)])

        self.index_dep_time = 0  # Index der nächsten Abreisezeit
        self.index_ar_time = 0  # Index der nächsten Ankunftszeitszeit

        self._waiting_time = [0]  # Wartezeit der/des wartenden Kunden
        self.number_waiting_people = [0]  # Anzahl der wartenden Personen

        self.average_processing_time = None
        self.average_waiting_time = None
        self.average_length_of_stay = None
        self.average_filling = None
        self.average_waiting_time = None

    @property
    def _arrival_time(self):
        """ Berechnung der Ankunftszeiten """
        return np.array([sum(self._distribution_arrival_time[:i]) for i in range(self.simulation_steps)])

    @property
    def _departure_time(self):
        """ Berechnung der Abreisezeit """
        departure_time = [self._arrival_time[0] + self._distribution_processing_time[0]]
        for i in range(self.simulation_steps-1):
            if departure_time[i] > self._arrival_time[i + 1]:
                departure_time.append(departure_time[i] + self._distribution_processing_time[i + 1])
            else:
                departure_time.append(self._arrival_time[i + 1] + self._distribution_processing_time[i + 1])

        return np.array(departure_time)

    def get_next_arrival_time(self):
        """ Rückgabe der nächsten Ankuftszeit"""
        return self._arrival_time[self.index_ar_time]

    def get_next_departure_time(self):
        """ Rückgabe der nächsten Abreisezeit"""
        return self._departure_time[self.index_dep_time]

    def get_waiting_time(self):
        """ Berechnen der Wartezeit für alle angekommen Kunden"""
        for i in range(self.index_ar_time - 1):
            if self._departure_time[i] - self._arrival_time[i + 1]:
                self._waiting_time.append(self._departure_time[i] - self._arrival_time[i + 1])
            else:
                self._waiting_time.append(0)

    def get_next_event(self):
        """Überprüfen ob nächstes Ereignis Anreise oder Abreise ist"""
        if self._arrival_time[self.index_ar_time] > self._departure_time[self.index_dep_time]:
            return "Departure"
        else:
            return "Arrival"

    def next_arrival(self):
        """ Aktualisieren der Zeit und Index Anreise erhöhen"""
        self.time.append(self._arrival_time[self.index_ar_time])
        self.index_ar_time += 1
        return self.time

    def next_departure(self):
        """ Aktualisieren der Zeit und Index Abreise erhöhen"""
        self.time.append(self._departure_time[self.index_dep_time])
        self.index_dep_time += 1
        return self.time

    def simulate_next_step(self):
        """ Entscheid ob Abreise oder Ankunft und aktualisieren der Anzahl der wartenden Personen """
        next_event = self.get_next_event()
        if next_event == "Arrival":
            self.next_arrival()
        else:
            self.next_departure()

        number_waiting_people = self.index_ar_time - self.index_dep_time - 1
        if number_waiting_people < 0: number_waiting_people = 0
        
        self.number_waiting_people.append(number_waiting_people)

        return self.time, self.number_waiting_people

    def calculate_average(self):
        """Es werden die Durchschnittswerte berechnet"""
        self.average_processing_time = sum(self._distribution_processing_time[:-self.index_dep_time]) / \
                                       len(self._distribution_processing_time[:-self.index_dep_time])
        self.average_waiting_time = sum(self._waiting_time) / len(self._waiting_time)
        self.average_length_of_stay = self.average_processing_time + self.average_waiting_time
        self.average_filling = sum(self.number_waiting_people) / len(self.number_waiting_people)

    def simulation_all(self):
        """ Ein gesamter Simulationsdurchlauf """
        for i in range(self.simulation_steps):
            self.simulate_next_step()
        self.get_waiting_time()
        self.calculate_average()
        return self.time, self.number_waiting_people

    def plot_time_numberwaiting_people(self,timeline, list_number_waiting_people):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.set_title(f"M/M/1 Warteschlangensystem\n"
                      f"$E_y={round(self.average_length_of_stay, 3)}; E_b={round(self.average_processing_time, 3)}; $"
                      f"$E_w={round(self.average_waiting_time, 3)}; max E_w = {round(max(self._waiting_time), 3)}; $"
                      f"max People={max(self.number_waiting_people)}", size=25)  # Erstellen vom Titel
        ax1.step(timeline, list_number_waiting_people)
        ax1.plot(timeline, list_number_waiting_people, 'ro')
        ax1.set_xlabel("Zeit", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der X-Achse
        ax1.set_ylabel("Anzahl der wartenden Personen", size=22, labelpad=20)  # Erstellen eines Schriftzugs an der Y-Achse
        ax1.tick_params(labelsize=20)  # Anpassen der Größe der Achsen Beschriftung
        ax1.grid()
        plt.show()


if __name__ == '__main__':
    franz_josef_strauß_check_in = CheckIn(0.6, 0.9, 100)
    t1 = franz_josef_strauß_check_in._departure_time
    t3 = franz_josef_strauß_check_in._distribution_processing_time
    t2 = franz_josef_strauß_check_in._arrival_time
    timeline, list_number_waiting_people = franz_josef_strauß_check_in.simulation_all()
    franz_josef_strauß_check_in.plot_time_numberwaiting_people(timeline, list_number_waiting_people)

