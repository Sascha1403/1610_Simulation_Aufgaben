import random
from typing import Sequence

from cellular_automaton import CellularAutomaton, MooreNeighborhood, CAWindow, EdgeRule


class Gruenalge(CellularAutomaton):

    def init_cell_state(self, __) -> Sequence:
        rand = random.randrange(0, 101, 1)
        init = max(.0, float(rand - 99))
        return [init * random.randint(0, 3)]

    def evolve_rule(self, __, neighbors_last_states: Sequence) -> Sequence:
        return self._neighborhood.get_neighbor_by_relative_coordinate(neighbors_last_states, (-1, -1))


def state_to_color(current_state: Sequence) -> Sequence:
    return 255 if current_state[0] == 1 else 0, \
           255 if current_state[0] == 2 else 0, \
           255 if current_state[0] == 3 else 0


neighborhood = MooreNeighborhood(EdgeRule.FIRST_AND_LAST_CELL_OF_DIMENSION_ARE_NEIGHBORS)

dimension = [20, 20]
CAWindow(cellular_automaton=Gruenalge(neighborhood=neighborhood, dimension=dimension),
         window_size=(1000, 830),
         state_to_color_cb=state_to_color).run(last_evolution_step=100, evolutions_per_second=0.5)
