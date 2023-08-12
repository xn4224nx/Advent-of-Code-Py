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

Part 2:
    How many lanternfish would there be after 256 days?

"""


class LanternFishes:

    def __init__(self, info_filepath: str):

        # Storage for fish by timer age
        self.pop_by_time = {x: 0 for x in range(9)}

        # Load the info file into memory
        self.pop = [int(x) for x in open(info_filepath, "r").read().split(",")]

        # Convert the population to a dictionary of all the states
        for fish in self.pop:
            self.pop_by_time[fish] += 1

    def pass_a_day(self):
        """
        Emulate a day passing on the lantern fish population.
        """

        # Decrease the internal timers of the fish by one
        new_pop = {x: 0 for x in range(9)}
        for timer in self.pop_by_time:

            if timer == 0:
                new_pop[6] += self.pop_by_time[timer]
                new_pop[8] += self.pop_by_time[timer]

            else:
                new_pop[timer-1] += self.pop_by_time[timer]

        self.pop_by_time = new_pop

    def run_simulation(self, days: int):
        """
        Simulate how the population will change over a set number of days.
        """

        for i in range(days):
            self.pass_a_day()

    def num_fish(self) -> int:
        """
        How many lantern Fish are there?
        """
        return sum([x for x in self.pop_by_time.values()])


# Read the initial population
sample = LanternFishes("./data/input.txt")

# Run a simulation
sample.run_simulation(80)
print(f"The answer to part 1: {sample.num_fish()}")

sample.run_simulation(256-80)
print(f"The answer to part 2: {sample.num_fish()}")
