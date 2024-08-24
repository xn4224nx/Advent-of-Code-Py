"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of
his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not
moving at all), and always spend whole seconds in either state.

PART 1: Given the descriptions of each reindeer (in your puzzle input), after
        exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

import re


def parse_data(file_path: str) -> dict[str : dict[str, int]]:
    """
    Read the reindeer data file and return a list of the reindeer details.
    """
    rein_re = re.compile(
        "".join([r"([A-Za-z]+) [\D]+ ([\d]+) [\D]+ ", r"([\d]+) [\D]+ ([\d]+)"])
    )
    all_results = {}

    with open(file_path) as fp:
        for line in fp.readlines():
            matches = rein_re.match(line)

            all_results[matches.group(1)] = {
                "fly_speed": int(matches.group(2)),
                "fly_time": int(matches.group(3)),
                "rest_time": int(matches.group(4)),
            }

    return all_results


def dist_trav(reindeer: dict[str, int], total_time):
    """
    A generator to determine how far each the reindeer has traveled up to this
    second. Each iteration is assumed to be one second passed.
    """
    secs_passed = 0
    speed = reindeer["fly_speed"]
    f_time = reindeer["fly_time"]
    r_time = reindeer["rest_time"]
    cycle_time = f_time + r_time

    while secs_passed <= total_time:
        secs_passed += 1

        # Calculate the total number of rest fly cycles that have been completed
        whole_cycles = secs_passed // cycle_time

        dist = whole_cycles * speed * f_time

        # Calculate the time into the current cycle
        rem_time = total_time - whole_cycles * (f_time + r_time)

        dist += min(rem_time, f_time) * speed

        yield dist


def race_winner_dist(all_rein: dict[str : dict[str, int]], total_time: int) -> int:
    """
    Find the distance traveled by the winning Reindeer.
    """
    dists = []

    for rein in all_rein.values():
        dists.append([x for x in dist_trav(rein, total_time)][-1])

    return max(dists)


if __name__ == "__main__":
    rein_data = parse_data("./data/input.txt")
    print(f"Part 1 = {race_winner_dist(rein_data, 2503)}")
