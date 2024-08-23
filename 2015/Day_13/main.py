"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not
everyone gets along! This year, you resolve, will be different. You're going to
find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their
happiness would increase or decrease if they were to find themselves sitting
next to each other person. You have a circular table that will be just big
enough to fit everyone comfortably, and so each person will have exactly two
neighbors.

PART 1: What is the total change in happiness for the optimal seating
        arrangement of the actual guest list?

In all the commotion, you realize that you forgot to seat yourself. At this
point, you're pretty apathetic toward the whole thing, and your happiness
wouldn't really go up or down regardless of who you sit next to. You assume
everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve
you a score of 0.

PART 2: What is the total change in happiness for the optimal seating
        arrangement that actually includes yourself?
"""

import re
from itertools import permutations


def parse_relationships(filepath: str) -> (dict[(str, str), int], list[str]):
    """
    Open the relationship file and transfrom it into a dictionary of tuples
    containing the two parties and the effect on the first persons
    happiness on being seated next to the other person. Also record the unique
    guests at the party in a list of strings.
    """
    re_pat = r"".join(
        [
            r"([a-zA-Z]+) would ([a-zA-Z]+) ",
            r"(\d+) happiness units ",
            r"by sitting next to ([a-zA-Z]+)",
        ]
    )

    rels = {}
    guests = set()
    happ = re.compile(re_pat)

    with open(filepath) as fp:
        for line in fp.readlines():
            mat = happ.match(line)

            if mat.group(2) == "gain":
                change = int(mat.group(3))
            else:
                change = -1 * int(mat.group(3))

            # Record relationships
            rels[(mat.group(1), mat.group(4))] = change

            # Record the guests
            guests.add(mat.group(1))
            guests.add(mat.group(4))

    return rels, list(guests)


def score_arrange(rels: dict[(str, str), int], guests: str) -> int:
    """
    Determine the happiness score of a particular seating arrangement.
    """
    happy_sum = 0

    for i in range(len(guests)):

        comp_0 = i
        comp_1 = i + 1

        # Compare the first & last guest relationships
        if comp_1 == len(guests):
            comp_1 = 0

        happy_sum += rels.get((guests[comp_0], guests[comp_1]), 0)
        happy_sum += rels.get((guests[comp_1], guests[comp_0]), 0)

    return happy_sum


def find_max_happy(
    rels: dict[(str, str), int], guests: list[str], me: bool = False
) -> int:
    """
    Find the seating arrangement that gives the maximum happiness by testing
    each combination of guest seating.
    """
    if me:
        guests.append("Me")

    return max([score_arrange(rels, comb) for comb in permutations(guests)])


if __name__ == "__main__":
    rels, guests = parse_relationships("./data/input.txt")
    print(f"Part 1 = {find_max_happy(rels, guests)}")
    print(f"Part 2 = {find_max_happy(rels, guests, True)}")
