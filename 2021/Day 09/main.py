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


def find_neighbours(
        heightmap: np.array, point: tuple[int, int]
) -> dict[tuple[int, int]: int]:
    """
    Find all the neighbouring points and their heights for one particular point
    `point`.
    """
    f_neighbours = {}

    # Check the x-axis
    if point[0] == 0:
        f_neighbours[point[0] + 1, point[1]] = heightmap[point[0] + 1, point[1]]

    elif point[0] == heightmap.shape[0] - 1:
        f_neighbours[point[0] - 1, point[1]] = heightmap[point[0] - 1, point[1]]

    else:
        f_neighbours[point[0] + 1, point[1]] = heightmap[point[0] + 1, point[1]]
        f_neighbours[point[0] - 1, point[1]] = heightmap[point[0] - 1, point[1]]

    # Check the y-axis
    if point[1] == 0:
        f_neighbours[point[0], point[1] + 1] = heightmap[point[0], point[1] + 1]

    elif point[1] == heightmap.shape[1] - 1:
        f_neighbours[point[0], point[1] - 1] = heightmap[point[0], point[1] - 1]

    else:
        f_neighbours[point[0], point[1] + 1] = heightmap[point[0], point[1] + 1]
        f_neighbours[point[0], point[1] - 1] = heightmap[point[0], point[1] - 1]

    return f_neighbours


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

            # Get the surrounding points
            neighbours = find_neighbours(heightmap, (i, j))

            # If all the surrounding tiles are higher this point is a low point
            if all(x > heightmap[i, j] for x in neighbours.values()):
                low_points.append((i, j))

    return low_points


def point_risk_level(
        heightmap: np.array, point_coords: list[tuple[int, int]]) -> list[int]:
    """
    Find the risk level of all the points in the list `points`.
    """
    return [heightmap[x]+1 for x in point_coords]


def descend_heightmap(
        heightmap: np.array, start_pnt: tuple[int, int]) -> tuple[int, int]:
    """
    Starting from a point find the lowest point is connected to and return that
    point.
    """

    # Loop until the lowest point has been found
    while True:

        # For the current point get its neighbours
        n_neighbours = find_neighbours(heightmap, start_pnt)

        # If all the surrounding points are the same or higher
        if all(x >= heightmap[start_pnt] for x in n_neighbours.values()):
            # Return the current point
            return start_pnt

        # Work out the lowest point in the neighbours
        else:
            # Then set `start_pnt` as that point
            start_pnt = min(n_neighbours, key=n_neighbours.get)


def find_basins(
        heightmap: np.array, low_points: list[tuple[int, int]]
) -> dict[tuple[int, int]: list[tuple[int, int]]]:
    """
    For a height map find the basins. Then return a list of the points in each
    basin.
    """

    # Key is the lowest point and value is a list of the basin points
    found_basins = {x: [] for x in low_points}

    # Iterate over every point and find its basin
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):

            # The highest point are not part of the basins
            if heightmap[i, j] == 9:
                continue

            # Detect low points
            if (i, j) in found_basins:
                found_basins[(i, j)].append((i, j))
                continue

            # For each point find the low point it belongs to
            pred_low_pnt = descend_heightmap(heightmap, (i, j))

            if pred_low_pnt not in found_basins:
                raise Exception(f"({pred_low_pnt[0]}, f"
                                "{pred_low_pnt[1]}) not found in low points")

            found_basins[pred_low_pnt].append((i, j))

    return found_basins


def calc_basin_multi_size(
        low_basins: dict[tuple[int, int]: list[tuple[int, int]]]) -> int:
    """
    Find the three largest basins and multiply their sizes together. Then return
    the integer size.
    """
    basin_sizes = sorted([len(x) for x in low_basins.values()])
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


if __name__ == "__main__":

    # Load the data
    height_map = load_heightmap("./data/input.txt")

    # Determine the location of low points in the height map
    low_point_coords = find_low_points(height_map)

    # Find the low point risk level
    risk_levels = point_risk_level(height_map, low_point_coords)

    print(f"The answer to part 1: {sum(risk_levels)}")

    # Find the basins
    basins = find_basins(height_map, low_point_coords)

    print(f"The answer to part 2: {calc_basin_multi_size(basins)}")
