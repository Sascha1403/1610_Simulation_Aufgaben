""" Aufgabe 4.1 """
# Importe
from ListSchueduler import ListSchuduler

# Parameter
resource = [2]
task_times = [5, 1, 1, 5]


# Klassen Initalisierung
LS = ListSchuduler(resource, task_times=task_times)

# Berechnung und Ausgabe der Task Times pro Ressource
total_time = LS.calculate_ressource_times()
LS.print_time(total_time=total_time)


""" Aufgabe 4.2 """
# Parameter festlegen
resources = [2, 4, 8, 16]
filename = "t-1-4.txt"

# Klassen Initalisierung
LS2 = ListSchuduler(resources, filename=filename)

# Berechnung und Ausgabe der Task Times pro Ressource
LS2.load_task_times()
total_time = LS2.calculate_ressource_times()
LS2.print_time(total_time=total_time)