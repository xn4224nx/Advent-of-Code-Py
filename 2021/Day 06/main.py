"""
--- Day 6: Lanternfish ---

A massive school of glowing lanternfish swims past. They must spawn quickly to
reach such large numbers - maybe exponentially quickly? You should model their
growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make
some guesses about their attributes. Surely, each lanternfish creates a new
lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish
- one lanternfish might have 2 days left until it creates another lanternfish,
while another might have 4. So, you can model each fish as a single number that
represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer
before it's capable of producing more lanternfish: two more days for its first
cycle.

Find a way to simulate lanternfish.

Part 1:
    How many lanternfish would there be after 80 days?

"""


class LanternFishes:

    def __init__(self, info_filepath: str):

        # Load the info file into memory
        self.pop = [int(x) for x in open(info_filepath, "r").read().split(",")]


# Read the initial population
sample = LanternFishes("./data/sample.txt")

print(sample.pop)
