"""
--- Day 1: Sonar Sweep ---

You're minding your own business on a ship at sea when the overboard alarm goes
off! You rush to see if you can help. Apparently, one of the Elves tripped and
accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for
situations like this.

As the submarine drops below the surface of the ocean, it automatically performs
a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report
(your puzzle input) appears: each line is a measurement of the sea floor depth
as the sweep looks further and further away from the submarine.

    Part 1: How many measurements are larger than the previous measurement?

    Part 2: Consider sums of a three-measurement sliding window. How many sums
            are larger than the previous sum?

"""


def sonar_sweep(heights: list, window_size: int) -> int:

    sweep_count = 0

    for x in range(len(heights) - window_size):

        # Record if the next window is larger than the current
        curr_wind = sum(heights[x: x + window_size])
        next_wind = sum(heights[x + 1: x + window_size + 1])

        if curr_wind < next_wind:
            sweep_count += 1

    return sweep_count


# Load the data
depths = [int(x) for x in open("./data/input.txt", "r").read().split()]

print(f"Part 1: Total increases = {sonar_sweep(depths, 1)}")
print(f"Part 1: Total window increases = {sonar_sweep(depths, 3)}")
