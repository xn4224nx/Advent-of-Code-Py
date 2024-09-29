"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the
clock's oscillator is regulated by stars. Unfortunately, the stars have been
stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve
all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter
Bunny Recruiting Document the Elves intercepted start here, and nobody had time
to work them out further.

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either
turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?

PART 1: How many blocks away is Easter Bunny HQ?

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

PART 2: How many blocks away is the first location you visit twice?
"""


def read_direction_data(file_path: str) -> list[list[str, int]]:
    """
    Parse the direction data from a file and return it in a list of tuples.
    """
    with open(file_path) as fp:
        return [[x[0], int(x[1:].strip())] for x in fp.read().split(", ")]


def directions_dist(directions: list[list[str, int]], repeat=False) -> int:
    """
    Calculate the distance from the start to the end point the directions
    take you too.
    """
    curr_dir = 1j  # You start pointing north
    curr_loc = 0 + 0j  # You start at the origin
    seen_locs = set()

    for turn, dist_mag in directions:
        if turn == "L":
            curr_dir *= 1j
        else:
            curr_dir *= -1j

        if repeat:
            # Save every point that the user passes through
            for i in range(1, dist_mag + 1):
                pnt = curr_loc + (curr_dir * i)

                # If the point has been seen before return the magnitude
                if pnt in seen_locs:
                    return int(abs(pnt.real) + abs(pnt.imag))
                else:
                    seen_locs.add(pnt)

        curr_loc += curr_dir * dist_mag

    return int(abs(curr_loc.real) + abs(curr_loc.imag))


if __name__ == "__main__":
    instrs = read_direction_data("./data/input.txt")
    print(f"Part 1 = {directions_dist(instrs)}")
    print(f"Part 2 = {directions_dist(instrs, True)}")
