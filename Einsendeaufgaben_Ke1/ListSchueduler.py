import random


class ListSchuduler:
    def __init__(self, resources,  **kwargs):
        self.resources = resources
        self.filename = kwargs.get('filename', None)
        self.task_times = kwargs.get('task_times', [])
        self.total_time = []
        self.equal_distribution = []
        self.gaussian_distribution = []

    def load_task_times(self):
        file = open(self.filename, 'r')
        f = file.readlines()
        for line in f:
            stringInput = line.split()
            self.task_times.append(int(stringInput[1]))
        return self.task_times

    def calculate_ressource_times(self, random_value=None):
        self.total_time = []
        if not self.task_times:
            raise Exception("Lade task_time oder Übergebe Sie als Parameter")

        if random_value == "Normalverteilung":
            equal_distribution = self.random_values_equal()

        if random_value == "Gaußverteilung":
            gaussian_distribution = self.random_values_gaussian()

        for i in range(len(self.resources)):
            resource_times = [0] * self.resources[i]

            for j in range(len(self.task_times)):
                if random_value == "Normalverteilung":
                    task_times = equal_distribution
                elif random_value == "Gaußverteilung":
                    task_times = gaussian_distribution
                else:
                    task_times = self.task_times

                lowestTime = min(resource_times)
                index = resource_times.index(lowestTime)
                resource_times[index] = resource_times[index] + task_times[j]
            self.total_time.append(max(resource_times))
        return self.total_time

    def random_values_gaussian(self):
        gaussian_distributen = [random.normalvariate(self.task_times[i], 0.15 * self.task_times[i])
                                for i in range(len(self.task_times))]
        return gaussian_distributen

    def random_values_equal(self):
        uniform_distribution = [random.uniform(0.7 * self.task_times[i], 1.3 * self.task_times[i])
                                for i in range(len(self.task_times))]
        return uniform_distribution

    ### Hier bin stehen geblieben  ###
    def caluclate_simulation(self, rounds, random_value=None):
        total_times = []
        [total_times.append([]) for i in range(len(self.resources))]

        for i in range(rounds):
            total_time = self.calculate_ressource_times(random_value)

            for j in range(len(total_time)):
                total_times[j].append(total_time[j])


        return total_times



    def print_time(self,**kwargs):
        total_time = kwargs.get('total_time', None)
        total_times = kwargs.get('total_times', None)
        random_value = kwargs.get('random_value', "deterministisch Verteilt")
        
        if total_times is not None:
            for i in range(len(total_times)):
                print("Für eine {} mit {} Resourcen ist ist max Bearbeitungszeit: {}\n"
                      "und die durchschnittliche Bearbeitungszeit: {}".format(random_value,
                                                                              self.resources[i], max(total_times[i]),
                                                                              (sum(total_times[i]) / len(total_times[i]))))

        if total_time is not None:
            for i in range (len(total_time)):
                print("Für {} Resourcen ist die Bearbeitungszeit: {}".format(self.resources[i], total_time[i]))




if __name__ == "__main__":
    resource = [1, 2]
    task_times = [5, 1, 1, 5]
    rounds = 1000
    filename = "t-1-4.txt"
    LS2 = ListSchuduler(resource, task_times=task_times)
    LS = ListSchuduler(resource, filename=filename)
    LS.load_task_times()
    total_time = LS.calculate_ressource_times()
    LS.print_time(total_time=total_time)
