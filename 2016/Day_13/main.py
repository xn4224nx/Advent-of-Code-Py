"""
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less
welcoming environment than the shiny atrium of the last one. Instead, you are in
a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers
(x,y). Each such coordinate is either a wall or an open space. You can't move
diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward
positive x and y; negative values are invalid, as they represent a location
outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is
actually quite logical. You can determine whether a given x,y coordinate will be
a wall or an open space using a simple system:

    -   Find x*x + 3*x + 2*x*y + y + y*y.

    -   Add the office designer's favorite number (your puzzle input).

    -   Find the binary representation of that sum; count the number of bits
        that are 1:

            -   If the number of bits that are 1 is even, it's an open space.

            -   If the number of bits that are 1 is odd, it's a wall.

PART 1: What is the fewest number of steps required for you to reach 31,39?

PART 2: How many locations (distinct x,y coordinates, including your starting
        location) can you reach in at most 50 steps?
"""


class Maze:
    def __init__(self, favorite_number: int):
        self.fav_num = favorite_number

    def is_wall(self, point: tuple[int, int]) -> bool:
        """
        Determine if a point is a wall and cannot be traversed.
        """
        x = point[0]
        y = point[1]

        # Calcuate a specific value using the point and a favorite number then
        # count the number of 1s in the binary form of the number.
        num_ones = (x * x + 3 * x + 2 * x * y + y + y * y + self.fav_num).bit_count()

        # If there are an odd number of ones it is a wall
        return num_ones % 2 != 0

    def poss_moves(self, start_point: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Find, from a starting point all possible next moves and the points the
        move would take it. Diagonal moves are not possible, only up, down, left
        and right.
        """
        s_x = start_point[0]
        s_y = start_point[1]
        pos_moves = []

        # Up
        up = (s_x, s_y - 1)
        if s_y != 0 and not self.is_wall(up):
            pos_moves.append(up)

        # Down
        dwn = (s_x, s_y + 1)
        if not self.is_wall(dwn):
            pos_moves.append(dwn)

        # Left
        lft = (s_x - 1, s_y)
        if s_x != 0 and not self.is_wall(lft):
            pos_moves.append(lft)

        # Right
        rgt = (s_x + 1, s_y)
        if not self.is_wall(rgt):
            pos_moves.append(rgt)

        return pos_moves

    def find_min_path_len(self, dest_point: tuple[int, int]) -> int:
        """
        Find the minimum length of the path through the maze to a specific
        point. I assume that no point should be traversed twice.
        """
        curr_pnts = [(1, 1)]
        seen_pnts = set()
        total_moves = 0

        # Iterate until the end point is reached
        while True:
            nxt_pnts = []
            total_moves += 1

            # Find the possible next moves and mark the current ones as seen
            for pnt in curr_pnts:
                seen_pnts.add(pnt)

                # If a point has been visited before don't visit it again
                for np_pnt in self.poss_moves(pnt):
                    if np_pnt not in seen_pnts:
                        nxt_pnts.append(np_pnt)

            if not nxt_pnts:
                raise Exception("There are no viable next moves!")

            # See if the destination has been reached
            if dest_point in nxt_pnts:
                break

            curr_pnts = nxt_pnts

        return total_moves

    def reached_locations(self, max_moves: int) -> int:
        """
        Find the unique locations that are reached within a maximum number of
        moves.
        """
        curr_pnts = [(1, 1)]
        seen_pnts = set()

        for mv_idx in range(max_moves):
            nxt_pnts = []

            # Find the possible next moves and mark the current ones as seen
            for pnt in curr_pnts:
                seen_pnts.add(pnt)

                # If a point has been visited before don't visit it again
                for np_pnt in self.poss_moves(pnt):
                    if np_pnt not in seen_pnts:
                        nxt_pnts.append(np_pnt)

            if not nxt_pnts:
                raise Exception("There are no viable next moves!")

            curr_pnts = nxt_pnts

        # Add in the final set of points
        for pnt in curr_pnts:
            seen_pnts.add(pnt)

        return len(seen_pnts)


if __name__ == "__main__":
    cubicles = Maze(1358)
    print(f"Part 1 = {cubicles.find_min_path_len((31,39))}")
    print(f"Part 2 = {cubicles.reached_locations(50)}")
