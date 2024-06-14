"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of
his reindeer is fastest, and so he has them race.

Given the descriptions of each reindeer (in your puzzle input), after exactly
2503 seconds, what distance has the winning reindeer traveled?
"""

import re


def distance_flown(reign_data, race_time):
    """Calculate the speed a reindeer moves in the time"""

    speed = int(reign_data[1])
    fly_time = int(reign_data[2])
    rest_time = int(reign_data[3])

    # determine the complete number of fly rest cycles the reindeer completes
    complete_cycles = race_time // (fly_time + rest_time)
    distance = complete_cycles * speed * fly_time

    # Determine the time remaining
    time_remain = race_time - complete_cycles * (fly_time + rest_time)

    # Work out how much flying is done in the time remaining
    if time_remain > fly_time:
        distance += (fly_time * speed)
    else:
        distance += (speed * time_remain)

    return distance


# Load the data
data = open("data/input.txt").read().splitlines()

# Parse the data
re_reindeer = r"(\w+) can fly (\d+) \D+ (\d+) \D+ (\d+)"
data = [re.findall(re_reindeer, x)[0] for x in data]

# Calculate the distance each Reindeer went (Part 1)
results = [distance_flown(x, 2503) for x in data]
print(max(results))

# Work out the position over time of each reindeer

# Keep a record of the scores of each reindeer
scores = [0 for i in range(len(data))]

# Iterate over the time of the race and calculate the distance each reindeer
# has travelled.
for elapsed_time in range(1, 2503+1):

    # For each one calculate how far they have flown
    cur_dists = [distance_flown(x, elapsed_time) for x in data]

    # Work out the furthest a reindeer has traveled
    max_dist = max(cur_dists)

    # Update the scores for the furthest traveled
    for i in range(len(cur_dists)):
        if cur_dists[i] == max_dist:
            scores[i] += 1

# Part 2 answer
print(max(scores))

