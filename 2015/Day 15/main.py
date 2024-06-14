"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
list of the remaining ingredients you could use to finish the recipe (your
puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

The total score of a cookie can be found by adding up each of the properties
(negative totals become 0) and then multiplying together everything except
calories.

Given the ingredients in your kitchen and their properties, what is the total
score of the highest-scoring cookie you can make?
"""
import re
from itertools import product


def cookie_score(cookie_data, weight_dist, calories=False) -> int:
    sum_scores = {}

    # Iterate over the cookie data
    for ingredient, info_dict in cookie_data.items():
        for name, value in info_dict.items():

            # If the characteristic of the cookie is not in the dict, add it
            if name not in sum_scores:
                sum_scores[name] = 0

            # Calculate the scores
            sum_scores[name] += value * weight_dist[ingredient]

    # Correct negative totals
    sum_scores = {name: (x + abs(x))//2 for name, x in sum_scores.items()}

    # Calculate the calories
    if calories and sum_scores['calories'] != 500:
        return 0

    # calculate total score
    total_score = [x for name, x in sum_scores.items() if name != 'calories']

    product_score = 1

    for score in total_score:
        product_score *= score

    return product_score


# Import data
data = open("data/input.txt").read().splitlines()

# Parse the data into a dict
re_cookie = r"(\w+): (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), " \
            r"(\w+) (-?\d+), (\w+) (-?\d+)"

data = [re.findall(re_cookie, x)[0] for x in data]

data = {info[0]: {info[1]: int(info[2]), info[3]: int(info[4]),
                  info[5]: int(info[6]), info[7]: int(info[8]),
                  info[9]: int(info[10])} for info in data}

# Generate all valid cookie ingredient combinations 0 - 100
ingredients = [x for x in data]
max_amount = 100
min_amount = 0
sum_amount = 100

scores = []
scores2 = []

for comb in product([x for x in range(min_amount, max_amount + 1)],
                    repeat=len(ingredients)):

    # Reject unusable combinations
    if sum(comb) != sum_amount:
        continue

    # Create weight_dist
    tmp_weights = {ingredients[i]: comb[i] for i in range(len(comb))}

    # Calculate Score
    scores.append(cookie_score(data, tmp_weights))
    scores2.append(cookie_score(data, tmp_weights, True))

# Part 1
print(max(scores))

# Part 2
print(max(scores2))
