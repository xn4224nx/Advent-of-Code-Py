"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of
his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not
moving at all), and always spend whole seconds in either state.

PART 1: Given the descriptions of each reindeer (in your puzzle input), after
        exactly 2503 seconds, what distance has the winning reindeer traveled?

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old
scoring system.

Instead, at the end of each second, he awards one point to the reindeer
currently in the lead. (If there are multiple reindeer tied for the lead, they
each get one point.) He keeps the traditional 2503 second time limit, of
course, as doing otherwise would be entirely ridiculous.

PART 2: Again given the descriptions of each reindeer (in your puzzle input),
        after exactly 2503 seconds, how many points does the winning reindeer
        have?
"""

import re


def parse_data(file_path: str) -> list[dict[str, int]]:
    """
    Read the reindeer data file and return a list of the reindeer details.
    """
    rein_re = re.compile(
        "".join([r"([A-Za-z]+) [\D]+ ([\d]+) [\D]+ ", r"([\d]+) [\D]+ ([\d]+)"])
    )
    all_results = []

    with open(file_path) as fp:
        for line in fp.readlines():
            matches = rein_re.match(line)

            all_results.append(
                {
                    "fly_speed": int(matches.group(2)),
                    "fly_time": int(matches.group(3)),
                    "rest_time": int(matches.group(4)),
                }
            )

    return all_results


def dist_trav(reindeer: dict[str, int], total_time):
    """
    A generator to determine how far each the reindeer has traveled up to this
    second. Each iteration is assumed to be one second passed.
    """
    speed = reindeer["fly_speed"]
    f_time = reindeer["fly_time"]
    r_time = reindeer["rest_time"]
    cycle_time = f_time + r_time

    # Calculate the total number of rest fly cycles that have been completed
    whole_cycles = total_time // cycle_time

    dist = whole_cycles * speed * f_time

    # Calculate the time into the current cycle
    rem_time = total_time - whole_cycles * (f_time + r_time)

    dist += min(rem_time, f_time) * speed

    return dist


def race_winner_dist(all_rein: list[dict[str, int]], total_time: int) -> (int, int):
    """
    Find the distance traveled by the winning Reindeer.
    """

    scores = [0 for _ in range(len(all_rein))]

    # Determine the reindeer who is in the lead for each second of the race
    for elap_sec in range(1, total_time + 1):
        dists = []

        # Calculate the distance traveled by each Reindeer
        for rein_dta in all_rein:
            dists.append(dist_trav(rein_dta, elap_sec))

        curr_max_dist = max(dists)

        # Increase the score of each reindeer in the lead
        for idx in range(len(dists)):
            if dists[idx] == curr_max_dist:
                scores[idx] += 1

    return max(dists), max(scores)


if __name__ == "__main__":
    rein_data = parse_data("./data/input.txt")
    win_dist, win_score = race_winner_dist(rein_data, 2503)

    print(f"Part 1 = {win_dist}\nPart 2 = {win_score}")
