"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at
most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal
lighting configuration. With so few lights, he says, you'll have to resort to
animation.

Start by setting your lights to the included initial configuration (your puzzle
input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next
configuration based on the current one. Each light's next state (either on or
off) depends on its current state and the current states of the eight lights
adjacent to it (including diagonals). Lights on the edge of the grid might
have fewer than eight neighbors; the missing ones always count as "off".

The state a light should have next is based on its current state (on or off)
plus the number of neighbors that are on:

    -   A light which is on stays on when 2 or 3 neighbors are on, and turns
        off otherwise.

    -   A light which is off turns on if exactly 3 neighbors are on, and stays
        off otherwise.

All of the lights update simultaneously; they all consider the same current
state before moving to the next.

PART 1: In your grid of 100x100 lights, given your initial configuration, how
        many lights are on after 100 steps?
"""

import numpy as np


def read_lights(file_path: str) -> np.array:
    """
    Read a file that describes the configuration of lights at a certain point
    in time and return a numpy array of booleans, with true representing on
    and false representing off.
    """
    raw_lines = []

    with open(file_path) as fp:
        for line in fp.readlines():
            line = line.strip()

            # Replace # with 1 and . with 0
            line = line.replace("#", "1")
            line = line.replace(".", "0")

            # Convert the string to a list of booleans
            raw_lines.append([bool(int(x)) for x in line])

    # Convert the list of lists to a numpy array of booleans
    return np.array(raw_lines, dtype="bool")


def find_adj_coords(
    grid_size: tuple[int, int], point: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    For a grid of a certain size and a particular point return a list of the
    adjacent points to the original.
    """
    adj_points = []

    # Row above the point
    if point[1] > 0:
        adj_points.append((point[0], point[1] - 1))

        if point[0] > 0:
            adj_points.append((point[0] - 1, point[1] - 1))

        if point[0] < grid_size[0] - 1:
            adj_points.append((point[0] + 1, point[1] - 1))

    # The row in line with the point
    if point[0] > 0:
        adj_points.append((point[0] - 1, point[1]))

    if point[0] < grid_size[0] - 1:
        adj_points.append((point[0] + 1, point[1]))

    # The row below the point
    if point[1] < grid_size[1] - 1:
        adj_points.append((point[0], point[1] + 1))

        if point[0] > 0:
            adj_points.append((point[0] - 1, point[1] + 1))

        if point[0] < grid_size[0] - 1:
            adj_points.append((point[0] + 1, point[1] + 1))

    return adj_points


def new_light_value(grid: np.array, point: tuple[int, int]) -> bool:
    """
    Determine what the new value of a light should be based on the rules in
    part 1.
    """
    l_state = grid[point[0]][point[1]]

    adj_lights = find_adj_coords(grid.shape, point)

    # Determine the number of adj_lights that are on
    num_on_lights = sum([grid[x][y] for x, y in find_adj_coords(grid.shape, point)])

    if l_state and num_on_lights in [2, 3]:
        return True

    if not l_state and num_on_lights == 3:
        return True

    return False


def step_lights(old_lights: np.array, num_steps: int) -> np.array:
    """
    Increment the given light grid by the rules described in part 1.
    """
    for _ in range(num_steps):

        new_lights = np.full(old_lights.shape, False, dtype="bool")

        # For each light determine it's new state.
        for x in range(old_lights.shape[1]):
            for y in range(old_lights.shape[0]):
                new_lights[x][y] = new_light_value(old_lights, (x, y))

        old_lights = new_lights

    return old_lights


if __name__ == "__main__":
    lights = read_lights("./data/input.txt")
    print(f"Part 1 = {sum(step_lights(lights, 100)).sum()}")
