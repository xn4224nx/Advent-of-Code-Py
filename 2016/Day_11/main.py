"""
--- Day 11: Radioisotope Thermoelectric Generators ---

You come upon a column of four floors that have been entirely sealed off from
the rest of the building except for a small dedicated lobby. There are some
radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to
experiment with Radioisotope Thermoelectric Generators (RTGs, or simply
"generators") that are designed to be paired with specially-constructed
microchips. Basically, an RTG is a highly radioactive rock that generates
electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously
radioactive. The chips are prototypes and don't have normal radiation
shielding, but they do have the ability to generate an electromagnetic
radiation shield when powered. Unfortunately, they can only be powered by their
corresponding RTG. An RTG powering a microchip is still dangerous to other
microchips.

In other words, if a chip is ever left in the same area as another RTG, and
it's not connected to its own RTG, the chip will be fried. Therefore, it is
assumed that you will follow procedure and keep chips connected to their
corresponding RTG when they're in the same room, and away from other RTGs
otherwise.

These microchips sound very interesting and useful to your current activities,
and you'd like to try to retrieve them. The fourth floor of the facility has an
assembling machine which can make a self-contained, shielded computer for you
to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have
these pre-assembly RTGs), there is an elevator that can move between the four
floors. Its capacity rating means it can carry at most yourself and two RTGs or
microchips in any combination. (They're rigged to some heavy diagnostic
equipment - the assembling machine will detach it for you.) As a security
measure, the elevator will only function if it contains at least one RTG or
microchip. The elevator always stops on each floor to recharge, and this takes
long enough that the items within it and the items on that floor can irradiate
each other. (You can prevent this if a Microchip and its Generator end up on
the same floor in this way, as they can be connected while the elevator is
recharging.)

You make some notes of the locations of each component of interest (your puzzle
input). Before you don a hazmat suit and start moving things around, you'd like
to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the
first floor.

PART 1: In your situation, what is the minimum number of steps required to
        bring all of the objects to the fourth floor?

You step into the cleanroom separating the lobby from the isolated area and put
on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra
parts on the first floor that weren't listed on the record outside:

    -   An elerium generator.
    -   An elerium-compatible microchip.
    -   A dilithium generator.
    -   A dilithium-compatible microchip.

These work just like the other generators and microchips. You'll have to get
them up to assembly as well.

PART 2: What is the minimum number of steps required to bring all of the
        objects, including these four new ones, to the fourth floor?
"""

import re
from itertools import combinations
import sys
import random


class RTGMover:
    """
    Determine the minimum number of moves required to move all the microchips
    and generators to the top floor.
    """

    def __init__(self, data_file: str, extra_ele=False):
        self.data_file = data_file
        self.max_floor = 0

        # If the file exists iterate over it line by line
        if self.data_file != "":
            micrs = {}
            gens = {}

            # Find the key parts of the data file
            with open(self.data_file) as fp:
                for idx, line in enumerate(fp):
                    self.max_floor = idx

                    # Find all the generators in the line
                    for gen_nm in re.findall(r"(\w+) generator", line):
                        gens[gen_nm] = idx

                    # Find all the microchips in the line
                    for micr_nm in re.findall(r"(\w+)-compatible microchip", line):
                        micrs[micr_nm] = idx

            #  Extra parts on the first floor
            if extra_ele:
                micrs["elerium"] = 0
                gens["elerium"] = 0
                micrs["dilithium"] = 0
                gens["dilithium"] = 0

            # Construct the state tuple
            g_state = []
            m_state = []
            self.names = []

            for element in sorted(gens.keys()):
                g_state.append(int(gens[element]))
                m_state.append(int(micrs[element]))
                self.names.append(element)

            self.state = [0] + g_state + m_state
            self.num_ele = int((len(self.state) - 1) / 2)

    def is_state_valid(self, state: list[int]) -> bool:
        """
        Determine if a state could be valid. This is primaraly done by ensuring
        that no microchip is on a level with another generator unless its
        matching one is on the same level.
        """
        for ele_idx in range(self.num_ele):

            # microchips and generators on the same level are safe
            if state[ele_idx + 1] == state[ele_idx + self.num_ele + 1]:
                continue

            # Otherwise check no other generator is on the same level
            for gen_lvl in state[1 : self.num_ele + 1]:
                if gen_lvl == state[ele_idx + self.num_ele + 1]:
                    return False

        return True

    def determine_valid_moves(self, state: list[int]) -> list[str]:
        """
        Provide a list of the next possible states the instance could be in.
        """
        new_positions = []

        # Create one item shift up or down
        for idx in range(1, len(state)):

            # Check the elevator is on the same level
            if state[idx] != state[0]:
                continue

            # Move down
            if state[idx] > 0:
                tmp_state = state.copy()
                tmp_state[0] -= 1
                tmp_state[idx] -= 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

            # Move up
            if state[idx] < self.max_floor:
                tmp_state = state.copy()
                tmp_state[0] += 1
                tmp_state[idx] += 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

        # Create two items shift up or down
        for idx_0, idx_1 in combinations([x for x in range(1, len(state))], 2):

            # Check the elevator is on the same level as both elements
            if state[idx_0] != state[0] or state[idx_1] != state[0]:
                continue

            # Move down
            if state[idx_0] > 0:
                tmp_state = state.copy()
                tmp_state[0] -= 1
                tmp_state[idx_0] -= 1
                tmp_state[idx_1] -= 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

            # Move up
            if state[idx_0] < self.max_floor:
                tmp_state = state.copy()
                tmp_state[0] += 1
                tmp_state[idx_0] += 1
                tmp_state[idx_1] += 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

        return new_positions

    def show(self) -> str:
        """
        Return a string representation of the current state of the building
        """
        result = ""

        # Iterate from the top floor to the lowest
        for idx in range(self.max_floor, -1, -1):

            # Add in the level details
            result += f"F{idx+1} "

            # Add in the elevator if it exists
            if self.state[0] == idx:
                result += "E  "
            else:
                result += ".  "

            # Complete each element in turn
            for ele_idx, ele_name in enumerate(self.names):

                # Lookup the generator
                if self.state[1 + ele_idx] == idx:
                    result += f"{ele_name.upper()[0]}G "
                else:
                    result += ".  "

                # Lookup the microchip
                if self.state[1 + ele_idx + self.num_ele] == idx:
                    result += f"{ele_name.upper()[0]}M "
                else:
                    result += ".  "

            # Add in the new line
            result += "\n"

        return result

    def convert_state(self, state: list[int]) -> str:
        """
        Convert the integer list state into a string one with ordered
        subsections of microchips and generators
        """
        return "".join([str(x) for x in state])

    def deconvert_state(self, state: str) -> list[int]:
        """
        Convert a string state to a list version
        """
        return [int(x) for x in state]

    def solve_bfs(self) -> int:
        """
        Attempt to find the solution with a breadth first search.
        """
        seen_states = set()
        curr_state = set()
        moves = 0

        seen_states.add(self.convert_state(self.state))
        curr_state.add(self.convert_state(self.state))

        while True:
            moves += 1
            next_states = set()

            for stored_state in curr_state:

                # Convert to a list version
                state = self.deconvert_state(stored_state)

                # Find the next possible states
                for nxt_state in self.determine_valid_moves(state):

                    # Check for a solution
                    if sum(nxt_state) == len(nxt_state) * self.max_floor:
                        return moves

                    # Convert to a string form
                    stored_nxt_state = self.convert_state(nxt_state)

                    # Check it has not been seem or store the state
                    if stored_nxt_state in seen_states:
                        continue
                    else:
                        seen_states.add(stored_nxt_state)

                    # Record the state for the next iteration
                    next_states.add(stored_nxt_state)

            # Check there are possible states
            if not next_states:
                raise Exception("No possible next moves possible!")

            # Overwrite the current states
            else:
                curr_state = next_states


if __name__ == "__main__":
    facility = RTGMover("./data/input.txt")
    print(f"Part 1 = {facility.solve_bfs()}")

    ex_facility = RTGMover("./data/input.txt", True)
    print(f"Part 2 = {ex_facility.solve_bfs()}")
