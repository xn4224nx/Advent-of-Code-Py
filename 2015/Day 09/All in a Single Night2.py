# -*- coding: utf-8 -*-
"""

--- Day 9: All in a Single Night ---

What is the distance of the shortest route?

Created on Sat Dec 31 22:43:04 2022

@author: FAKENAME
"""

import re

graph_re = r"([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)"

# Load the data from the file
data = open("sample.txt").read().splitlines()

# Parse the distance data
loc_data = [re.findall(graph_re, x) for x in data]

# 

