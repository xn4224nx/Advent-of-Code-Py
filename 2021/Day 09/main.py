"""
--- Day 9: Smoke Basin ---

Smoke flows to the lowest point of the area it's in.

Each number corresponds to the height of a particular location, where 9 is the
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than
any of its adjacent locations. Most locations have four adjacent locations (up,
down, left, and right); locations on the edge or corner of the map have three or
two adjacent locations, respectively. (Diagonal locations do not count as
adjacent.)

The risk level of a low point is 1 plus its height.

Part 1:
    Find all of the low points on your heightmap. What is the sum of the risk
    levels of all low points on your heightmap?

"""