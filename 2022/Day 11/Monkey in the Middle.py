# -*- coding: utf-8 -*-
"""

--- Day 11: Monkey in the Middle ---

Figure out which monkeys to chase by counting how many items they inspect
over 20 rounds. What is the level of monkey business after 20 rounds of
stuff-slinging simian shenanigans?

Created on Sat Dec 24 12:26:57 2022

@author: FAKENAME
"""

import math

def calc_opperation(start_val, opp_ls):
    """
    Calculates what start value should be after the opperation detailed
    in the opperation list. Possible opperations are:

        * - times
        + - add
    """

    # Detect the first variable
    if opp_ls[0] == "old":
        first_var = start_val

    else:
        first_var = int(opp_ls[0])

    # Detect the last vaiable
    if opp_ls[2] == "old":
        last_var = start_val

    else:
        last_var = int(opp_ls[2])

    # Detect opperation type
    if opp_ls[1] == '+':
        return first_var + last_var

    elif opp_ls[1] == '*':
        return first_var * last_var


# Load Instructions
instrucs = open("input.txt", "r").read().splitlines()

# Parse the Monkey data into a dict
monkey_dict = {}

for line in instrucs:

    # The start of monkey data
    if "Monkey " in line:

        monk = int(line.replace("Monkey ", "").replace(":", "").strip())

        monkey_dict[monk] = {"total": 0}

    # Starting Items data
    elif "Starting items: " in line:

        # Extract the item data
        items_str = line.replace("Starting items:", "").strip().split(',')

        # Parse as integers and save to the dict
        monkey_dict[monk]["items"] = [int(x.strip()) for x in items_str]

    # Operation data
    elif "Operation: " in line:

        # Extract the item data
        item_str = line.replace("Operation: new = ", "").strip().split()

        # Parse the data and save to the dict
        monkey_dict[monk]["oper"] = item_str

    # Test data
    elif "Test: " in line:

        # Extract the item data
        item_str = int(line.replace("Test: divisible by ", "").strip())

        # Parse the data and save to the dict
        monkey_dict[monk]["test"] = item_str

    # Test Results - True
    elif "If true:" in line:

        # Extract the item data
        item_str = int(line.replace("If true: throw to monkey ", "").strip())

        # Parse the data and save to the dict
        monkey_dict[monk]["true"] = item_str

    # Test Results - False
    elif "If false:" in line:

        # Extract the item data
        item_str = int(line.replace("If false: throw to monkey ", "").strip())

        # Parse the data and save to the dict
        monkey_dict[monk]["false"] = item_str

# Find the factor to remove from the large numbers
factors = [int(y["test"]) for x, y in monkey_dict.items()]

large_num_factor = math.prod(factors)

# Simulate many rounds of stuff-slinging simian shenanigans
for i in range(10000):

    print(f"Round {i}")

    # Iterate over the monkey data dict
    for monkey, data in monkey_dict.items():

        # print(f"Monkey {monkey}:")

        # Iterate over each item a monkey has
        for item in data["items"]:

            # Stop the numbers from getting too large
            item %= large_num_factor

            # print(f"\t\tMonkey inspects an item with "
            #       f"a worry level of {item}.")

            # Perform the opperation on the items worry value
            item = calc_opperation(item, data["oper"])

            # print(f"\t\tWorry level is changed to {item}")

            # Divide by three and round down
            # item //= 3

            # print("\t\tMonkey gets bored with item. Worry"
            #       f" level is divided by 3 to {item}.")

            # Test what the monkey does with the item
            if item % data["test"] == 0:

                # print(f"\t\tCurrent worry level "
                #       f"is divisible by {data['test']}.")
                dest_monk = data['true']
            else:

                # print(f"\t\tCurrent worry level is not "
                #       f"divisible by {data['test']}.")
                dest_monk = data['false']

            # Add the item to another monkeys list
            monkey_dict[dest_monk]["items"].append(item)
            # print(f"\t\tItem with worry level {item} is "
            #       f"thrown to monkey {dest_monk}.", end="\n\n")

            # Increment the total items seen
            monkey_dict[monkey]["total"] += 1

        # Empty the current monkeys items
        monkey_dict[monkey]["items"] = []


# After a number of rounds calculate the total amount of monkey business
total = sorted([y["total"] for x, y in monkey_dict.items()], reverse=True)

monkey_business = total[0] * total[1]

print(f"Total monkey business is {monkey_business}.")
