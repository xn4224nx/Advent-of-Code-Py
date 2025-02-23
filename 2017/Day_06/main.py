"""
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory
reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any
number of blocks. The goal of the reallocation routine is to balance the blocks
between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory
bank with the most blocks (ties won by the lowest-numbered memory bank) and
redistributes those blocks among the banks. To do this, it removes all of the
blocks from the selected bank, then moves to the next (by index) memory bank
and inserts one of the blocks. It continues doing this until it runs out of
blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a
blocks-in-banks configuration is produced that has been seen before.

The debugger would like to know how many redistributions can be done before a
blocks-in-banks configuration is produced that has been seen before.

        -   The banks start with 0, 2, 7, and 0 blocks. The third bank has the
            most blocks, so it is chosen for redistribution.

        -   Starting with the next bank (the fourth bank) and then continuing
            to the first bank, the second bank, and so on, the 7 blocks are
            spread out over the memory banks. The fourth, first, and second
            banks get two blocks each, and the third bank gets one back. The
            final result looks like this: 2 4 1 2.

        -   Next, the second bank is chosen because it contains the most blocks
            (four). Because there are four memory banks, each gets one block.
            The result is: 3 1 2 3.

        -   Now, there is a tie between the first and fourth memory banks, both
            of which have three blocks. The first bank wins the tie, and its
            three blocks are distributed evenly over the other three banks,
            leaving it with none: 0 2 3 4.

        -   The fourth bank is chosen, and its four blocks are distributed such
            that each of the four banks receives one: 1 3 4 1.

        -   The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was already
seen. The infinite loop is detected after the fifth block redistribution cycle,
and so the answer in this example is 5.

PART 1: Given the initial block counts in your puzzle input, how many
        redistribution cycles must be completed before a configuration is
        produced that has been seen before?

Out of curiosity, the debugger would also like to know the size of the loop:
starting from a state that has already been seen, how many block redistribution
cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer
in that example would be 4.

PART 2: How many cycles are in the infinite loop that arises from the
        configuration in your puzzle input?
"""


class MemoryBank:
    def __init__(self, initial_state_file: str):
        self.state = []

        with open(initial_state_file, "r") as fp:
            for mem in fp.read().strip().split():
                self.state.append(int(mem))

    def max_bank(self) -> int:
        """
        Find the index of largest memory bank.
        """
        curr_max = 0
        curr_max_idx = 0

        for idx in range(len(self.state)):
            if self.state[idx] > curr_max:
                curr_max = self.state[idx]
                curr_max_idx = idx

        return curr_max_idx

    def redistribute(self):
        """
        Take the memory from the largest bank and incrementally redistribute it
        to every other memory bank.
        """
        max_idx = self.max_bank()
        max_value = self.state[max_idx]

        # Set the max value to zero
        self.state[max_idx] = 0

        # Increase the other banks in order from the one that was reduced
        for bnk_idx in range(1, max_value + 1):
            incres_idx = (max_idx + bnk_idx) % len(self.state)
            self.state[incres_idx] += 1

    def steps_until_loop(self) -> (int, int):
        """
        Find the redistribution steps required to see a state of the memory bank
        that has already been seen before. Return the steps take to detect a
        loop and the loop size
        """
        num_steps = 0
        seen_states = {}

        # Loop until a previously seen state is encountered
        while True:

            # Check if the new state has been seen before
            if tuple(self.state) in seen_states:
                break

            # Record the step when this state was encountered
            seen_states[tuple(self.state)] = num_steps

            self.redistribute()
            num_steps += 1

        return num_steps, num_steps - seen_states[tuple(self.state)]


if __name__ == "__main__":
    steps_to_loop, loop_len = MemoryBank("./data/input.txt").steps_until_loop()
    print(f"Part 1 = {steps_to_loop}")
    print(f"Part 2 = {loop_len}")
