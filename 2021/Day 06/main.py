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

    def pass_a_day(self):
        """
        Emulate a day passing on the lantern fish population.
        """

        # Decrease the internal timers of the fish by one
        self.pop = [x-1 for x in self.pop]

        # If there is lantern fish that will divide reset the timer and add one
        if -1 in self.pop:

            # Count of replicating fish
            rep_fish = self.pop.count(-1)

            # Replace the `-1` with `6`
            self.pop = [6 if x == -1 else x for x in self.pop]

            # Add in the new fishes
            self.pop += [8 for x in range(rep_fish)]

    def run_simulation(self, days: int):
        """
        Simulate how the population will change over a set number of days.
        """

        for i in range(days):
            self.pass_a_day()


# Read the initial population
sample = LanternFishes("./data/sample.txt")

# Run a simulation
sample.run_simulation(80)
print(f"The answer to part 1: {len(sample.pop)}")
