# -*- coding: utf-8 -*-
"""

--- Day 6: Tuning Trouble ---

Created on Tue Dec  6 17:57:02 2022

@author: FAKENAME

How many characters need to be processed before the
first start-of-packet marker is detected?
"""

# The numbers of unique chars needed
window = 14

# Load the stream of data from file
data_stream = open("input.txt", "r").read()

# Loop over the stream
for i in range(window, len(data_stream)):

    # partition the stream into window sized chunks
    wind_str = data_stream[i-window:i]

    # Check if the chunk contains unique values
    if len(set(wind_str)) == window:
        print(f"Char Processed = {i}")
        break
