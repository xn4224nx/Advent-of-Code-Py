"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
list of the remaining ingredients you could use to finish the recipe (your
puzzle input) and their properties per teaspoon:

    *   capacity (how well it helps the cookie absorb milk)

    *   durability (how well it keeps the cookie intact when full of milk)

    *   flavor (how tasty it makes the cookie)

    *   texture (how it improves the feel of the cookie)

    *   calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you
have to be accurate so you can reproduce your results in the future. The total
score of a cookie can be found by adding up each of the properties (negative
totals become 0) and then multiplying together everything except calories.

PART 1: Given the ingredients in your kitchen and their properties, what is
        the total score of the highest-scoring cookie you can make?
"""

from itertools import combinations_with_replacement, permutations
import re


def parse_property_data(file_path: str) -> dict[str : dict[str:int]]:
    """
    Read the ingredients data file and transform it into a nested hashmap format.
    """
    ret = {}

    with open(file_path) as fp:
        for line in fp.readlines():
            name, details = line.split(":")

            ret[name] = {}

            for match in re.finditer(r"([A-Za-z]+) (-?\d)", details):
                ret[name][match.group(1)] = int(match.group(2))

    return ret


def score_weight_comb(
    properties: dict[str : dict[str:int]], weight_comb: dict[str:int]
) -> int:
    score = 1

    for attr in ["capacity", "durability", "flavor", "texture"]:
        score *= max(
            sum(
                [
                    properties[name][attr] * weight
                    for name, weight in weight_comb.items()
                ]
            ),
            0,
        )

    return score


def weight_combinations(ingredients: list[str], total_weight: int) -> dict[str:int]:
    """
    Generate the possible combinations of the ingredients weights.
    """
    pos_weights = [x for x in range(total_weight + 1)]

    # Iterate over all possible combinations of weights
    for comb in combinations_with_replacement(pos_weights, len(ingredients)):

        # Only combinations that sum are valid
        if sum(comb) != total_weight:
            continue

        # Iterate over every possible permutation of ingredient weights
        for perm in permutations(comb):
            yield {x: y for x, y in zip(ingredients, perm)}


def find_best_score(properties: dict[str : dict[str:int]], total_weight: int) -> int:
    """
    For a combination of ingredients and total weight find the best score
    possible.
    """
    best_score = 0

    for comb in weight_combinations(list(properties.keys()), total_weight):
        best_score = max(score_weight_comb(properties, comb), best_score)

    return best_score


if __name__ == "__main__":
    ingre_prop = parse_property_data("./data/input.txt")
    print(f"Part 1 = {find_best_score(ingre_prop, 100)}")
