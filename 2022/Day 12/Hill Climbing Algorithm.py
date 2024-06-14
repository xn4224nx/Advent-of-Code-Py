# -*- coding: utf-8 -*-
"""

--- Day 12: Hill Climbing Algorithm ---

What is the fewest steps required to move from your current position
to the location that should get the best signal?

current position (S)
best signal (E)

During each step, you can move exactly one square up, down, left,
or right. To avoid needing to get out your climbing gear, the
elevation of the destination square can be at most one higher than
the elevation of your current square; that is,
if your current elevation is m, you could step to
elevation n, but not to elevation o. (This also means
that the elevation of the destination square can be much
lower than the elevation of your current square.)

Created on Sat Dec 24 18:11:19 2022

@author: FAKENAME
"""

import numpy as np
import random

class Navigate_Map:

    def __init__(self, map_file):

        # Start and end position for the map
        self.start_pos = None
        self.end_pos = None

        # Load the map file
        instrucs = open(map_file, "r").read().splitlines()

        self.x_len = len(instrucs)
        self.y_len = len(instrucs[0])

        # Coordinates in the map
        self.map_coords = []

        # Numerical elevation map
        self.el_map = np.zeros((self.x_len, self.y_len), dtype=int)

        # Parse the map into a matrix of numerical elevations
        for i in range(self.x_len):
            for j in range(self.y_len):

                # Catch the start position
                if instrucs[i][j] == 'S':
                    self.el_map[i, j] = 0
                    self.start_pos = (i, j)

                # Catch the end position
                elif instrucs[i][j] == 'E':
                    self.el_map[i, j] = 25
                    self.end_pos = (i, j)

                # Convert the letters to an elevation
                else:
                    self.el_map[i, j] = ord(instrucs[i][j]) - ord('a')

                # Save a record of the map coordinates
                self.map_coords.append((i, j))

    def cell_height(self, cell_coord):
        """
        Find the height of the map cell at cell_coord.
        """
        return self.el_map[cell_coord[0], cell_coord[1]]

    def all_cells_of_height(self, height):
        """
        Find all cells of a particular height in the map.
        """

        cells_of_height = []

        # Loop over the map
        for i in range(self.x_len):
            for j in range(self.y_len):

                if self.el_map[i, j] == height:
                    cells_of_height.append((i, j))

        return cells_of_height

    def avaliable_moves(self, cell_coord):
        """
        For an (x,y) tuple of coordinates find the possible moves that can be
        made and returns a list of tubles of the possible move coordinates.
        """

        # Current cell's coordinates
        x = cell_coord[0]
        y = cell_coord[1]

        # The cells up down left and right to the current cell
        near_cells = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

        # Check none of the cells are off the map
        near_cells = [cell for cell in near_cells if cell[0] >= 0 and cell[1]
                      >= 0 and cell[0] < self.x_len and cell[1]
                      < self.y_len]

        near_by_height = []

        # For each of the availabe cells check that its not too high
        for cell in near_cells:

            if self.cell_height(cell)+1 >= self.cell_height(cell_coord):
                # if self.cell_height(cell)-1 <= self.cell_height(cell_coord):
                near_by_height.append(cell)

        return near_by_height

    def paths_between(self, start_coord, end_coord):
        """
        Find the paths between start_coord and end_coord.
        """

        # Distance Nodes for the paths, default to infinity
        dist_node = {x: np.inf for x in self.map_coords}

        # Set the distance between the start_coord and itself to zero
        dist_node[start_coord] = 0

        # Nodes to visit
        nodes_to_visit = {x: None for x in self.map_coords}

        # Start node
        curr_node = start_coord

        while (nodes_to_visit):

            curr_dist = dist_node[curr_node]

            # Nodes to visit, sub nodes of curr_node
            sub_nodes = self.avaliable_moves(curr_node)

            # Don't re-visit nodes
            sub_nodes = [x for x in sub_nodes if x in nodes_to_visit]

            # Update the distance values
            for node in sub_nodes:
                dist_node.update({node: curr_dist+1})

            if end_coord in sub_nodes:
                break

            # Remove curr_node from nodes_to_visit
            del nodes_to_visit[curr_node]

            # Pick a new random node with the lowest distance
            # to be the current node

            min_node_val = np.inf
            min_node_coord = None

            for node in nodes_to_visit:

                # Test to see if its the closest
                if dist_node[node] < min_node_val:
                    min_node_val = dist_node[node]
                    min_node_coord = node

            if min_node_coord is None:
                return None

            else:
                curr_node = min_node_coord

        return dist_node[end_coord]

    def paths_to_end(self, end_coord):
        """
        Finds the distance from every coordinate to `end_coord`
        """

        # Distance Nodes for the paths, default to infinity
        dist_node = {x: np.inf for x in self.map_coords}

        # Set the distance between the end_coord and itself to zero
        dist_node[end_coord] = 0

        # Nodes to visit
        nodes_to_visit = {x: None for x in self.map_coords}

        # Set the current node as the end node
        curr_node = end_coord

        # Make sure all nodes have been visited
        while (nodes_to_visit):

            # Current distance from the `end_coord`
            curr_dist = dist_node[curr_node]

            # Nodes to visit, sub nodes of curr_node
            sub_nodes = self.avaliable_moves(curr_node)

            # Don't re-visit nodes
            sub_nodes = [x for x in sub_nodes if x in nodes_to_visit]

            # Update the distance values
            for node in sub_nodes:
                dist_node.update({node: curr_dist+1})

            # Remove curr_node from nodes_to_visit
            del nodes_to_visit[curr_node]

            # Pick a new random node with the lowest distance
            # to be the current node

            min_node_val = np.inf
            min_node_coord = None

            for node in nodes_to_visit:

                # Test to see if its the closest
                if dist_node[node] < min_node_val:
                    min_node_val = dist_node[node]
                    min_node_coord = node

            if min_node_coord is None:
                break

            else:
                curr_node = min_node_coord

        return dist_node


# Parse the map
e_map = Navigate_Map("input.txt")

# Find all path lengths to the end point
paths_to_end = e_map.paths_to_end(e_map.end_pos)

# Part 1
print(f"Part 1: {paths_to_end[e_map.start_pos]}")

# Part 2

min_path = np.min([paths_to_end[x] for x in e_map.all_cells_of_height(0)])
print(f"Part 2: {int(min_path)}")
