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


class RTGMover:
    """
    Determine the minimum number of moves required to move all the microchips
    and generators to the top floor.
    """

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.state = {"E": 0}
        self.max_floor = 0

        # If the file exists iterate over it line by line
        if self.data_file != "":
            with open(self.data_file) as fp:
                for idx, line in enumerate(fp):
                    self.max_floor = idx

                    # Find all the generators in the line
                    for gen in re.findall(r"(\w+) generator", line):
                        self.state[gen[0].upper() + "G"] = idx

                    # Find all the microchips in the line
                    for micr in re.findall(r"(\w+)-compatible microchip", line):
                        self.state[micr[0].upper() + "M"] = idx

    def is_state_valid(self, state: dict[str, int]) -> bool:
        """
        Determine if a state could be valid. This is primaraly done by ensuring
        that no microchip is on a level with another generator unless its
        matching one is on the same level.
        """
        for obj, level in state.items():
            if obj == "E" or obj[1] == "G":
                continue

            # Check if a microchip is protected by its counterpart
            if state[obj[0] + "G"] == level:
                continue

            # Otherwise check if another generator is on the same level
            for obj_2, level_2 in state.items():
                if obj_2 == "E" or obj_2[1] == "M":
                    continue

                if obj_2[1] == "G" and level_2 == level:
                    return False

        # If none of the microchips got fried this state is valid
        return True

    def determine_valid_moves(self) -> list[dict[str, int]]:
        """
        Provide a list of the next possible states the instance could be in.
        """
        new_positions = []
        pos_objs = [x for x in self.state.keys() if x != "E"]

        # Create one item shift up or down
        for obj in combinations(pos_objs, 1):
            obj = obj[0]

            # An object needs to be on the same floor as the elevator
            if self.state[obj] != self.state["E"]:
                continue

            # A move down
            if self.state[obj] > 0:
                new_state = self.state.copy()
                new_state[obj] -= 1
                new_state["E"] -= 1

                if self.is_state_valid(new_state):
                    new_positions.append(new_state)

            # A move up
            if self.state[obj] < self.max_floor:
                new_state = self.state.copy()
                new_state[obj] += 1
                new_state["E"] += 1

                if self.is_state_valid(new_state):
                    new_positions.append(new_state)

        # Create two items shift up or down
        for obj_0, obj_1 in combinations(pos_objs, 2):

            # Ensure both objects and the elevator are on the same floor
            if self.state[obj_0] == self.state["E"] == self.state[obj_1]:

                # A double up move
                if self.state[obj_0] > 0:
                    new_state = self.state.copy()
                    new_state[obj_0] -= 1
                    new_state[obj_1] -= 1
                    new_state["E"] -= 1

                    if self.is_state_valid(new_state):
                        new_positions.append(new_state)

                # A double down move
                if self.state[obj_0] < self.max_floor:
                    new_state = self.state.copy()
                    new_state[obj_0] += 1
                    new_state[obj_1] += 1
                    new_state["E"] += 1

                    if self.is_state_valid(new_state):
                        new_positions.append(new_state)
        print(new_positions)

        return new_positions

    def solve(self) -> int:
        """
        Find the minimum number of moves to transfer all the objects to the
        top floor.
        """
        pass

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
            if self.state["E"] == idx:
                result += "E  "
            else:
                result += ".  "

            # Add in the objects that are in
            for obj, level in sorted(self.state.items()):
                if obj == "E":
                    continue

                if level == idx:
                    result += f"{obj} "
                else:
                    result += ".  "

            # Add in the new line
            result += "\n"

        return result


if __name__ == "__main__":
    pass
