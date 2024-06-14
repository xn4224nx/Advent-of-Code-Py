"""
--- Day 18: Like a GIF For Your Yard ---

Start by setting your lights to the included initial configuration (your puzzle
input). A # means "on", and a . means "off".

Each light's next state (either on or off) depends on its current state and the
current states of the eight lights adjacent to it (including diagonals). Lights
on the edge of the grid might have fewer than eight neighbors; the missing ones
always count as "off".

The state a light should have next is based on its current state (on or off)
plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off
    otherwise.

    A light which is off turns on if exactly 3 neighbors are on, and stays off
    otherwise.

All of the lights update simultaneously; they all consider the same current
state before moving to the next.
"""


class LightGrid:
    def __init__(self, path_to_text_file, corners_on=False) -> None:
        self.on_char = '#'
        self.off_char = '.'
        self.path_to_text_file = path_to_text_file
        self.corners_on = corners_on

        # Load the text file from disk and use to populate a light grid
        self.light_grid = open(self.path_to_text_file).read().splitlines()

        # Parse the data into a structured array
        self.light_grid = [list(row) for row in self.light_grid]

        # Determine the shape of the light grid
        self.shape = (len(self.light_grid[0]), len(self.light_grid))

        # The corner lights are always on
        if self.corners_on:
            self.light_grid[0][0] = self.on_char
            self.light_grid[0][self.shape[0]-1] = self.on_char
            self.light_grid[self.shape[0]-1][0] = self.on_char
            self.light_grid[self.shape[0]-1][self.shape[0]-1] = self.on_char

    def __str__(self) -> str:
        """Return a string of the current light grid."""
        ret_str = ""

        for iy in range(self.shape[1]):
            for ix in range(self.shape[0]):
                ret_str += str(self.light_grid[iy][ix])
            ret_str += '\n'
        ret_str += '\n'

        return ret_str

    def is_light_on(self, ix, iy, outside_is_off=True) -> bool:
        """Works out if light in grid is on."""

        # Check if the light is in the grid
        if ix < 0 or ix >= self.shape[0] or iy < 0 or iy >= self.shape[1]:
            if outside_is_off:
                return False
            else:
                return True

        # Otherwise check what is in the grid
        if self.light_grid[iy][ix] == self.on_char:
            return True
        elif self.light_grid[iy][ix] == self.off_char:
            return False
        else:
            raise Exception(
                f"Light grid char {self.light_grid[iy][ix]} not recognised")

    def next_state(self) -> None:
        """
        Iterate over the grid and update it to what should be in
        the next iteration.
        """

        # Define a new empty grid to hold the values
        new_grid = [[None for ix in range(self.shape[0])]
                    for iy in range(self.shape[1])]

        # Loop over the values of the light grid to determine what the
        # new one should equal.
        for iy in range(self.shape[1]):
            for ix in range(self.shape[0]):

                # Count the number of neighbour lights that are on including
                # diagonals
                total_neigh_on = sum([
                    self.is_light_on(ix, iy + 1),
                    self.is_light_on(ix, iy - 1),
                    self.is_light_on(ix + 1, iy),
                    self.is_light_on(ix - 1, iy),
                    self.is_light_on(ix + 1, iy + 1),
                    self.is_light_on(ix - 1, iy - 1),
                    self.is_light_on(ix - 1, iy + 1),
                    self.is_light_on(ix + 1, iy - 1)
                ])

                # If the light is currently on
                if self.light_grid[iy][ix] == self.on_char:

                    if total_neigh_on in [2, 3]:
                        new_grid[iy][ix] = self.on_char
                    else:
                        new_grid[iy][ix] = self.off_char

                # If the light is currently off
                elif self.light_grid[iy][ix] == self.off_char:

                    if total_neigh_on in [3]:
                        new_grid[iy][ix] = self.on_char
                    else:
                        new_grid[iy][ix] = self.off_char

        # Overwrite the old grid with the new grid
        self.light_grid = new_grid.copy()

        # The corner lights are always on
        if self.corners_on:
            self.light_grid[0][0] = self.on_char
            self.light_grid[0][self.shape[0]-1] = self.on_char
            self.light_grid[self.shape[0]-1][0] = self.on_char
            self.light_grid[self.shape[0]-1][self.shape[0]-1] = self.on_char

    def num_lights_on(self) -> int:
        """How many lights are on in the grid"""
        on_count = 0

        for iy in range(self.shape[1]):
            for ix in range(self.shape[0]):
                if self.is_light_on(ix, iy):
                    on_count += 1

        return on_count


# Part 1
elf_grid = LightGrid("data/input.txt")
[elf_grid.next_state() for i in range(100)]
print(elf_grid.num_lights_on())
print(elf_grid)

# Part 2
elf_grid2 = LightGrid("data/input.txt", True)
[elf_grid2.next_state() for i in range(100)]
print(elf_grid2.num_lights_on())
print(elf_grid2)