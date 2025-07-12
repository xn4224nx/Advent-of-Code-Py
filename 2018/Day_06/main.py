"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like
you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal
interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they
places it thinks are safe or dangerous? It recommends you check manual page
729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by
counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For
example, consider the following list of coordinates:

    1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9

If we name these coordinates A through F, we can draw them on a grid, putting
0,0 at the top left:

    ..........
    .A........
    ..........
    ........C.
    ...D......
    .....E....
    .B........
    ..........
    ..........
    ........F.

This view is partial - the actual grid extends infinitely in all directions.
Using the Manhattan distance, each location's closest coordinate can be
determined, shown here in lowercase:

    aaaaa.cccc
    aAaaa.cccc
    aaaddecccc
    aadddeccCc
    ..dDdeeccc
    bb.deEeecc
    bBb.eeee..
    bbb.eeefff
    bbb.eeffff
    bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they
don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while
not shown here, their areas extend forever outside the visible grid. However,
the areas of coordinates D and E are finite: D is closest to 9 locations, and E
is closest to 17 (both including the coordinate's location itself). Therefore,
in this example, the size of the largest area is 17.

PART 1: What is the size of the largest area that isn't infinite?
"""

import sys


class MineField:
    def __init__(self, coord_file: str):
        self.mine_coords = []
        self.field_size = [0, 0]

        with open(coord_file, "r") as fp:
            for line in fp.readlines():
                pnt = tuple(map(int, line.split(", ", 1)))

                # Determine the furthest reach of the minefield
                for idx in range(2):
                    if pnt[idx] > self.field_size[idx]:
                        self.field_size[idx] = pnt[idx]

                self.mine_coords.append(pnt)
        self.field_size = tuple(self.field_size)

    def manhatt_dist(self, pnt0: (int, int), pnt1: (int, int)) -> int:
        """
        Calculate the Manhattan distance between two points,
        """
        return abs(pnt0[0] - pnt1[0]) + abs(pnt0[1] - pnt1[1])

    def largest_enclosed_space(self) -> int:
        """
        For the minefield determine the largest area within it that is not
        infinite.
        """
        near_sqrs = [1] * len(self.mine_coords)
        inf_area = [False] * len(self.mine_coords)

        # Check every square to find out what mine is closest
        for y_idx in range(self.field_size[1] + 1):
            for x_idx in range(self.field_size[0] + 1):
                pnt = (x_idx, y_idx)

                # The square the mine is on is always closest to it but that
                # is aleardy counted in `near_sqrs`
                if pnt in self.mine_coords:
                    continue

                # Determine the closest mine to this square
                min_dist = sys.maxsize
                closest_mine = 0
                tie_in_dist = False

                for mine_idx in range(len(self.mine_coords)):
                    dist = self.manhatt_dist(pnt, self.mine_coords[mine_idx])

                    if dist < min_dist:
                        min_dist = dist
                        closest_mine = mine_idx
                        tie_in_dist = False

                    elif dist == min_dist:
                        tie_in_dist = True

                # Ensure this distance is unique amd there isn't a tie
                if tie_in_dist:
                    continue

                # If this point is on the edge then the area covered by that
                # mine is infinite and it is excluded from the answer.
                if not inf_area[closest_mine] and (
                    pnt[0] == 0
                    or pnt[0] == self.field_size[0]
                    or pnt[1] == 0
                    or pnt[1] == self.field_size[1]
                ):
                    inf_area[closest_mine] = True

                # Increment the number of squares this mine is closest to
                near_sqrs[closest_mine] += 1

        # Find and return the mine with the largest enclosed area
        max_area = 0
        for mine_idx in range(len(self.mine_coords)):
            if inf_area[mine_idx]:
                continue

            if not inf_area[mine_idx] and near_sqrs[mine_idx] > max_area:
                max_area = near_sqrs[mine_idx]

        return max_area


if __name__ == "__main__":
    print(f"Part 1 = { MineField("./data/input_0.txt").largest_enclosed_space()}")
