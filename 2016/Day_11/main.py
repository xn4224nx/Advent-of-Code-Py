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

    def __init__(self, data_file: str):
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

    def determine_valid_moves(self) -> list[str]:
        """
        Provide a list of the next possible states the instance could be in.
        """
        new_positions = []

        # Create one item shift up or down
        for idx in range(1, len(self.state)):

            # Check the elevator is on the same level
            if self.state[idx] != self.state[0]:
                continue

            # Move down
            if self.state[idx] > 0:
                tmp_state = self.state.copy()
                tmp_state[0] -= 1
                tmp_state[idx] -= 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

            # Move up
            if self.state[idx] < self.max_floor:
                tmp_state = self.state.copy()
                tmp_state[0] += 1
                tmp_state[idx] += 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

        # Create two items shift up or down
        for idx_0, idx_1 in combinations([x for x in range(1, len(self.state))], 2):

            # Check the elevator is on the same level as both elements
            if self.state[idx_0] != self.state[0] or self.state[idx_1] != self.state[0]:
                continue

            # Move down
            if self.state[idx_0] > 0:
                tmp_state = self.state.copy()
                tmp_state[0] -= 1
                tmp_state[idx_0] -= 1
                tmp_state[idx_1] -= 1
                if self.is_state_valid(tmp_state):
                    new_positions.append(tmp_state)

            # Move up
            if self.state[idx_0] < self.max_floor:
                tmp_state = self.state.copy()
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

    def overall_level(self) -> int:
        """
        Calculate the total level of the elements in the levels
        """
        return sum(self.state)

    def solve(self) -> int:
        """
        Find the minimum number of moves to transfer all the objects to the
        top floor.
        """
        start_state = self.state
        num_iters = 1_000_000
        max_moves = 1000
        old_level = 0

        # Test minumum move length from one till the maximum
        for curr_max_move in range(10, max_moves + 1):

            # Try random moves
            for idx in range(num_iters):
                self.state = start_state

                for move_idx in range(curr_max_move):

                    # Find the next possible states
                    nxt_states = self.determine_valid_moves()

                    # Check there are possible states
                    if not nxt_states:
                        break

                    # Pick a random state and apply it
                    self.state = random.choice(nxt_states)

                    # Check to see if all the objects are on the top floor
                    if sum(self.state) == len(self.state) * self.max_floor:
                        return move_idx + 1

                    # Check that overall levels are increasing
                    if move_idx % 10 == 0 and move_idx > 0:

                        # Ensure that the level is going up
                        if old_level > sum(self.state):
                            break
                        else:
                            old_level = sum(self.state)

        return curr_min_mvs


if __name__ == "__main__":
    facility = RTGMover("./data/input.txt")
    print(f"Part 1 = {facility.solve()}")
