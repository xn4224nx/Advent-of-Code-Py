"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be a
graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles. You can't help but mark the
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

PART 1: In your puzzle input, how many of the listed triangles are possible?

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

PART 2: In your puzzle input, and instead reading by columns, how many of the
        listed triangles are possible?
"""


def read_triangle_data(file_path: str) -> list[tuple[int, int, int]]:
    """
    Open a file of triangle data and read the side lengths.
    """
    tri = []

    with open(file_path) as fp:
        for line in fp.read().splitlines():
            nums = line.split()
            tri.append((int(nums[0]), int(nums[1]), int(nums[2])))

    return tri


def is_valid_triangle(sides: tuple[int, int, int]) -> bool:
    """
    Determine if the given side lengths could be a valid triangle.
    """

    if sides[0] >= sides[1] + sides[2]:
        return False

    if sides[1] >= sides[0] + sides[2]:
        return False

    if sides[2] >= sides[0] + sides[1]:
        return False

    return True


def count_valid_triangles(multi_sides: list[tuple[int, int, int]]) -> int:
    """
    From a list of sides count the number of triangles that could be valid.
    """
    return sum([is_valid_triangle(tri) for tri in multi_sides])


if __name__ == "__main__":
    weird_triangles = read_triangle_data("./data/input.txt")
    print(f"Part 1 = {count_valid_triangles(weird_triangles)}")
