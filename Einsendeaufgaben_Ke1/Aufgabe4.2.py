""" Aufgabe 4.2 """
# Importe
from ListSchueduler import ListSchuduler

# Parameter festlegen
resources = [2, 4, 8, 16]
filename = "t-1-4.txt"

# Klassen Initalisierung
LS2 = ListSchuduler(resources, filename=filename)

# Berechnung und Ausgabe der Task Times pro Ressource
LS2.load_task_times()
total_time = LS2.calculate_ressource_times()
LS2.print_time(total_time=total_time)