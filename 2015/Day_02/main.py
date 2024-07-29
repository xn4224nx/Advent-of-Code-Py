"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to
submit an order for more. They have a list of the dimensions
(length l, width w, and height h) of each present, and only want
to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular
prism), which makes calculating the required wrapping paper for
each gift a little easier: find the surface area of the box, which
is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper
for each present: the area of the smallest side.

PART 1: All numbers in the elves' list are in feet. How many
        total square feet of wrapping paper should they order?
"""

import re


def calc_area(length: int, width: int, height: int) -> int:
    """
    What is the area of wrapping paper required of a certain box?
    This is calculated as the area of the box plus the area of the
    smallest side.
    """
    box_area = 2 * length * width + 2 * width * height + 2 * height * length
    sorted_sides = sorted([length, width, height])
    smallest_side = sorted_sides[0] * sorted_sides[1]

    return box_area + smallest_side


def sum_all_wrapping(all_box_dims: list[(int, int, int)]) -> int:
    """
    Calculate the total area of wrapping paper required to cover
    all the boxes defined in a list of tuples (all_box_dims).
    """

    wrp_sum = 0

    for length, width, height in all_box_dims:
        wrp_sum += calc_area(length, width, height)

    return wrp_sum


def parse_box_dims(dim_file: str) -> list[(int, int, int)]:
    """
    Read the text file that contains the dimesions of the boxes,
    one per line. And return a list of the sizes.
    [(length, width, height)]
    """

    box_dims = []

    # Read the file into an array of strings
    with open(dim_file) as fp:
        raw_dims = fp.readlines()

    # Cast each list as three integers
    for line in raw_dims:
        l_res = re.search(r"(\d+)x(\d+)x(\d+)", line)
        box_dims.append((int(l_res.group(1)), int(l_res.group(2)), int(l_res.group(3))))

    return box_dims


if __name__ == "__main__":
    box_dims = parse_box_dims("./data/input.txt")
    print(f"The answer to part 1 = {sum_all_wrapping(box_dims)}")
