"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all
into your refrigerator, you'll need to move it into smaller containers. You
take an inventory of the capacities of the available containers.

--- Part 1 ---
Filling all containers entirely, how many different combinations of containers
can exactly fit all 150 liters of eggnog?

--- Part 2 ---
Find the minimum number of containers that can exactly fit all 150 liters of
eggnog. How many different ways can you fill that number of containers and
still hold exactly 150 litres?

"""
from itertools import combinations

containers = [50,
              44,
              11,
              49,
              42,
              46,
              18,
              32,
              26,
              40,
              21,
              7,
              18,
              43,
              10,
              47,
              36,
              24,
              22,
              40]

container_combs = []

# Generate every possible combination of containers
for i in range(1, len(containers)):
    for comb in combinations(containers, r=i):

        # Test if the array of containers matches the needed capacity
        if sum(comb) == 150:
            container_combs.append(comb)

# Find min number needed
container_combs_len = [len(x) for x in container_combs]
min_con_needed = min(container_combs_len)

# Part 1
print(len(container_combs))

# Part 2
print(container_combs_len.count(min_con_needed))
