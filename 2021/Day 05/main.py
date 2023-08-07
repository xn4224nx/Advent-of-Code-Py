"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review.

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where
x1,y1 are the coordinates of one end the line segment and x2,y2 are the
coordinates of the other end. These line segments include the points at both
ends.

Part 1:
    Consider only horizontal and vertical lines. At how many points do at least
    two lines overlap?

"""


def load_vent_data(data_file: str) -> list[tuple[list[int], list[int]]]:

    # Load the raw data from file
    raw_data = open(data_file, "r").read().splitlines()

    # Parse the line coordinates
    vents = []
    for line in raw_data:

        # Split the two coordinates
        start, end = line.split(" -> ")

        # Convert the coordinates to integers
        start = [int(x) for x in start.split(",")]
        end = [int(x) for x in end.split(",")]

        vents.append((start, end))

    return vents


sample_data = load_vent_data("./data/sample.txt")

print(sample_data)