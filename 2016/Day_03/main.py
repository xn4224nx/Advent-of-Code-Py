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
"""


def read_triangle_data(file_path: str) -> list[tuple[int, int, int]]:
    """
    Open a file of triangle data and read the side lengths.
    """
    pass


def is_valid_triangle(sides: tuple[int, int, int]) -> bool:
    """
    Determine if the given side lengths could be a valid triangle.
    """
    pass


def count_valid_triangles(multi_sides: list[tuple[int, int, int]]) -> int:
    """
    From a list of sides count the number of triangles that could be valid.
    """
    pass


if __name__ == "__main__":
    pass
