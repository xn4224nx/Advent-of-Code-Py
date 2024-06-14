# -*- coding: utf-8 -*-
"""

Elf Calorie Counter

Created on Thu Dec  1 18:02:00 2022

@author: FAKENAME

Find the Elf carrying the most Calories. How many total
Calories is that Elf carrying?

"""

# Array to store the totals
elves_tot_cal = []

# Sum the total calories for each Elf
elf_cal = 0

# Read the input file into memory line by line
with open("input.txt") as file:

    for line in file:

        cleaned_line = line.rstrip()

        if cleaned_line == "":
            # Save the result for this elf
            elves_tot_cal.append(elf_cal)

            # Reset the total
            elf_cal = 0
        else:

            elf_cal += int(cleaned_line)

# Sort the results
elves_tot_cal.sort(reverse=True)

print(f"The Max calories and Elf has is {elves_tot_cal[0]}")

print(f"The sum of the calories of the top three elves"
      f" is {sum(elves_tot_cal[:3])}")