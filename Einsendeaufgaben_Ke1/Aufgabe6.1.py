""" Aufgabe 6.1 """
# Importe
from ListSchueduler import ListSchuduler

# Parameter
resource = [1, 4]
task_times = [1, 2, 2, 6, 6, 10, 1]

# Klasse Initalisieren
LS = ListSchuduler(resource, task_times=task_times)

# Berechnung und Ausgabe der Task Times pro Ressource
total_time = LS.calculate_ressource_times()
LS.print_time(total_time=total_time)


