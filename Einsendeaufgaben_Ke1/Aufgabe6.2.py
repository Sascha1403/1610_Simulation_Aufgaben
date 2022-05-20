""" Aufgabe 6.2 """
# Importe
from ListSchueduler import ListSchuduler

# Parameter
resource = [4]
task_times = [1, 2, 2, 6, 6, 10, 1]
rounds = 1000
random_gauß = "Gaußverteilung"
random_equal = "Normalverteilung"

# Klasse Initalisieren
LS = ListSchuduler(resource, task_times=task_times)
total_times_gauß = LS.caluclate_simulation(rounds, random_gauß)
total_times_equal = LS.caluclate_simulation(rounds, random_equal)
LS.print_time(total_times=total_times_equal, random_value=random_equal)
LS.print_time(total_times=total_times_gauß, random_value=random_gauß)

