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


def points_on_line(line: tuple[list[int], list[int]]) -> list:
    """
    Find all the points between and including two points.
    """

    # Vertical Line
    if line[0][0] == line[1][0]:

        # Find the smaller & larger number
        if line[0][1] > line[1][1]:
            up = line[0][1]
            dw = line[1][1]

        else:
            up = line[1][1]
            dw = line[0][1]

        return [(line[0][0], x) for x in range(dw, up+1)]

    # Horizontal Line
    elif line[0][1] == line[1][1]:

        # Find the smaller & larger number
        if line[0][0] > line[1][0]:
            up = line[0][0]
            dw = line[1][0]

        else:
            up = line[1][0]
            dw = line[0][0]

        return [(x, line[1][1]) for x in range(dw, up+1)]

    else:
        return []


# Load the sample data
sample_data = load_vent_data("./data/input.txt")

# For each point
vent_points = {}

for line_points in sample_data:

    # find all the points on the line
    points = points_on_line(line_points)

    for vent_pt in points:

        if vent_pt in vent_points:
            vent_points[vent_pt] += 1
        else:
            vent_points[vent_pt] = 1


# Count the points where two or more
overlapping_pts = len([x for x in vent_points if vent_points[x] > 1])

print(overlapping_pts)
