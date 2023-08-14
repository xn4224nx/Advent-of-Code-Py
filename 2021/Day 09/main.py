"""
--- Day 9: Smoke Basin ---

Smoke flows to the lowest point of the area it's in.

Each number corresponds to the height of a particular location, where 9 is the
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than
any of its adjacent locations. Most locations have four adjacent locations (up,
down, left, and right); locations on the edge or corner of the map have three or
two adjacent locations, respectively. (Diagonal locations do not count as
adjacent.)

The risk level of a low point is 1 plus its height.

Part 1:
    Find all of the low points on your heightmap. What is the sum of the risk
    levels of all low points on your heightmap?

Part 2:
    What do you get if you multiply together the sizes of the three largest
    basins?

"""

import numpy as np


def load_heightmap(file_path: str) -> np.array:
    """
    Load the heightmap from file and parse it into an numpy array.
    """
    raw_data = []

    for line in open(file_path, "r").read().splitlines():
        raw_data.append([int(x) for x in line])

    data = np.array(raw_data)

    return data


def find_low_points(heightmap: np.array) -> list[tuple[int, int]]:
    """
    Find the positions of the low points in a heightmap and return a list of
    tuples of the coordinates of the heightmap.
    """
    # Determine the low points in the height map
    low_points = []

    # Iterate over every point in the height map
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):

            # If all the surrounding tiles are higher this point is a low point
            check = []

            # Check the x axis
            if i == 0:
                check.append(heightmap[i, j] < heightmap[i+1, j])

            elif i == heightmap.shape[0]-1:
                check.append(heightmap[i, j] < heightmap[i-1, j])

            else:
                check.append(heightmap[i, j] < heightmap[i+1, j])
                check.append(heightmap[i, j] < heightmap[i-1, j])

            # Check the y axis
            if j == 0:
                check.append(heightmap[i, j] < heightmap[i, j+1])

            elif j == heightmap.shape[1]-1:
                check.append(heightmap[i, j] < heightmap[i, j-1])

            else:
                check.append(heightmap[i, j] < heightmap[i, j+1])
                check.append(heightmap[i, j] < heightmap[i, j-1])

            if all(check):
                low_points.append((i, j))

    return low_points


def point_risk_level(
        heightmap: np.array, point_coords: list[tuple[int, int]]) -> list[int]:
    """
    Find the risk level of all the points in the list `points`.
    """

    # Find the risk levels of the points
    return [heightmap[x]+1 for x in point_coords]


if __name__ == "__main__":

    # Load the data
    height_map = load_heightmap("./data/input.txt")

    # Determine the location of low points in the height map
    low_point_coords = find_low_points(height_map)

    # Find the low point risk level
    risk_levels = point_risk_level(height_map, low_point_coords)

    print(f"The answer to part 1: {sum(risk_levels)}")
