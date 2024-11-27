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


class RTGMover:
    """
    Determine the minimum number of moves required to move all the microchips
    and generators to the top floor.
    """

    def __init__(self, data_file: str):
        pass

    def determine_valid_moves(self) -> list[dict[str, int]]:
        """
        Provide a list of the next possible states the instance could be in.
        """
        pass

    def is_state_valid(self, state: dict[str, int]) -> bool:
        """
        Determine if a state could be valid.
        """
        pass

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
        pass


if __name__ == "__main__":
    pass
