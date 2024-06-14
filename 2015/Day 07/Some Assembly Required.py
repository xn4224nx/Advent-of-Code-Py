# -*- coding: utf-8 -*-
"""
--- Day 7: Some Assembly Required ---

Created on Fri Dec 30 14:49:25 2022

@author: FAKENAME

what signal is ultimately provided to wire a?
"""


def execute_comands():

    # Dictionary to store the lines that have not been executed
    unused_lines = {}

    # Get the initial assignments in the instructions
    for line in data:

        command = line.split(line_split_str)

        # If the command is just a number
        if command[0].isdigit():

            # Save the value to the wires dict if it has not already been set
            if wires[command[1]] is None:

                wires[command[1]] = int(command[0])
                print(line)

        # Else add the lines to unused line array
        else:
            unused_lines[line] = None

    # Execute all the commands
    while unused_lines:

        executed_lines = []

        # Search the instructions for ones that all the numbers are known
        for line in unused_lines:

            # Split the command by spaces
            command, destination = line.split(line_split_str)

            # Find the wires in the command
            ln_wires = [x for x in command.split()
                        # exclude commands and numbers
                        if x not in pos_commands and not x.isdigit()]

            # Detect if the components of the command are known,
            # if not skip this line in the instructions
            if [x for x in ln_wires if wires[x] is None]:
                continue

            # Get the wires and numbers in the command
            values = [x for x in command.split() if x not in pos_commands]

            # Replace the values with there true values
            for i in range(len(values)):

                # Change pure numbers to integers
                if values[i].isdigit():
                    values[i] = int(values[i])

                # Lookup the name of the variable in the wires dict
                else:
                    values[i] = wires[values[i]]

            # Parse the command
            if " AND " in line:
                wires[destination] = (values[0] & values[1]) & 0xFFFF

            elif " OR " in line:
                wires[destination] = (values[0] | values[1]) & 0xFFFF

            elif " LSHIFT " in line:
                wires[destination] = (values[0] << values[1]) & 0xFFFF

            elif " RSHIFT " in line:
                wires[destination] = (values[0] >> values[1]) & 0xFFFF

            elif "NOT " in line:
                # Complement and then turn -ve numbers to unsigned value
                wires[destination] = (~ values[0]) & 0xFFFF

            else:
                # Assignment
                wires[destination] = values[0]

            # if the line was sucessfully executed remove if from the dict
            executed_lines.append(line)
            print(line)

        # Remove the executed lines from the unused_lines dict
        [unused_lines.pop(x) for x in executed_lines]

        # Every loop iteration lines should be exceuted,
        # if none are break the loop.
        if not executed_lines:
            break


# Load the data
data = open("input.txt").read().splitlines()

# Possible commands
pos_commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
line_split_str = " -> "

# Work out the wires in the circuit
wires = {x: None for x in set([x.split(line_split_str)[1] for x in data])}

execute_comands()

part_1_ans = wires['a']

print(f"\n\nThe answer to part 1 is {part_1_ans}")

# Reset the other values
wires = {x: None for x in set([x.split(line_split_str)[1] for x in data])}

# take the signal you got on wire a, override wire b to that signal
wires['b'] = part_1_ans

execute_comands()

print(f"\n\nThe answer to part 2 is {wires['a']}")
