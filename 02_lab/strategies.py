import self as self

from state import *
from random import shuffle


class Strategy:
    def __init__(self, state: State):
        self.state = state

    def backtracking(self, next_state: State):
        if check_final_state(next_state):
            print(f'INFO\tSolution was found.')
            exit(0)

        for i in range(len(next_state.shore) - 1):
            if not next_state.shore[i] and not next_state.shore[i + 1] and\
                    validate_transition(next_state, i, i + 1, FORWARD):
                candidate = transition(next_state, i + 1, FORWARD)
                print(f'INFO\tTrying {candidate.shore} | BOAT -> '
                      f'{"INITIAL_SHORE" if candidate.position_of_boat == INITIAL_SHORE else "FINAL_SHORE"}')

                self.backtracking(candidate)
                print('INFO\tBacktracking...')
            elif next_state.shore[i] and next_state.shore[i + 1] and \
                    validate_transition(next_state, i, i + 1, BACKWARDS):
                candidate = transition(next_state, i + 1, BACKWARDS)
                print(f'INFO\tTrying {candidate.shore} | BOAT -> '
                      f'{"INITIAL_SHORE" if candidate.position_of_boat == INITIAL_SHORE else "FINAL_SHORE"}')

                self.backtracking(candidate)
                print('INFO\tBacktracking...')

    @staticmethod
    def bfs():
        print('INFO\tNot implemented yet.')

    def hill_climbing(self, state: State):
        initial_state = create_initial_state(len(self.state.shore)//2)
        current_state = State(initial_state.shore.copy(), initial_state.position_of_boat)

        while True:
            best_neighbor = current_state.neighbor()

            if best_neighbor.evaluation() >= current_state.evaluation():
                return current_state.state
            current_state = best_neighbor

    @staticmethod
    def a_star():
        print('INFO\tNot implemented yet.')
