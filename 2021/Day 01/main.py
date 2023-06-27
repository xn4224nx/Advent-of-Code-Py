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

# Load the data
depths = [int(x) for x in open("./data/input.txt", "r").read().split()]

# Iterate over the loop and count when the loop decreases
increase_count = 0

for x in range(len(depths) - 1):

    # Record if the next measurement is larger than the current
    if depths[x] < depths[x + 1]:
        increase_count += 1

window_count = 0
for x in range(len(depths) - 3):

    # Record if the next window is larger than the current
    curr_wind = sum(depths[x:x+3])
    next_wind = sum(depths[x+1:x+4])

    if curr_wind < next_wind:
        print("increase")
        window_count += 1

print(f"Part 1: Total increases = {increase_count}")
print(f"Part 1: Total window increases = {window_count}")
