"""
--- Day 17: Spinlock ---

The Spinlock starts with a circular buffer containing only the value 0, which
it marks as the current position.

It then steps forward through the circular buffer some number of steps (your
puzzle input) before inserting the first new value, 1, after the value it
stopped on. The inserted value becomes the current position. Then, it steps
forward from there the same number of steps, and wherever it stops, inserts
after it the second new value, 2, and uses that as the new current position
again.

It repeats this process of stepping forward, inserting a new value, and using
the location of the inserted value as the new current position a total of 2017
times, inserting 2017 as its final operation, and ending with a total of 2018
values (including 0) in the circular buffer.

Part 1
What is the value after 2017 in your completed circular buffer?

Part 2
What is the value after 0 the moment 50000000 is inserted?


"""

from collections import deque


def spinlock(iterations: int, step_size: int) -> deque:

    # Create the spinlock
    ret_spinlock = deque([0])

    for i in range(1, iterations+1):
        ret_spinlock.rotate(-step_size)
        ret_spinlock.append(i)

    return ret_spinlock


# Part 1
part_1_spin = spinlock(2017, 370)
print(part_1_spin[0])

# Part 2
part_2_spin = spinlock(50_000_000, 370)
print(part_2_spin[part_2_spin.index(0) + 1])