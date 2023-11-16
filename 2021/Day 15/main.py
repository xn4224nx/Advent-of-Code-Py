"""
--- Day 15: Chiton ---

The cavern is large, but has a very low ceiling, restricting your motion to two
dimensions. The shape of the cavern resembles a square; a quick scan of chiton
density produces a map of risk level throughout the cave (your puzzle input).

You start in the top left position, your destination is the bottom right
position, and you cannot move diagonally. The number at each position is its
risk level; to determine the total risk of an entire path, add up the risk
levels of each position you enter (that is, don't count the risk level of your
starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk.

Part 1:
    What is the lowest total risk of any path from the top left to the bottom
    right?
"""

import numpy as np
import sys

class ChitonCave:

    def __init__(self, datafile: str):

        # Load the cave data from file and parse the risk map
        self.risk_map = np.array(
            [[int(x) for x in y] for y in
             open(datafile, "r").read().splitlines()])
        
        print(self.risk_map)
        
        # Define the start and end points
        self.start = (0, 0)
        self.end = (self.risk_map.shape[0]-1, self.risk_map.shape[1]-1)

    def find_lowest_risk_path(self):
        """
        Find the path with the lowest risk score between `start` and `end` using
        Dijkstra's algorithm. Use the algorithm listed here:
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        """
        
        # Set all points in the cave as sys.maxsize 
        pnt_dist = {(x, y): sys.maxsize 
                    for x in range(self.risk_map.shape[0]) 
                    for y in range(self.risk_map.shape[1])}

        # apart from the origin, which is set as zero
        pnt_dist[self.start] = 0
        
        # Mark all points as unvisited
        unvisited_points = set(pnt_dist.keys()) 
        
        # Start at the origin
        curr_node = self.start
        
        # Loop until the destination node has been visited
        while self.end in unvisited_points:
            
            print(f"\ncurrent node = {curr_node}")
            
            # For each neighbour calculate the risk
            neighb_pnts = []
            for nei_node in self.find_connected_points(curr_node):
                
                # Filter down to unvisited neighbours
                if nei_node not in unvisited_points:
                    continue
                
                # Calculate the risk for that node
                temp_dist = (
                    self.risk_map[curr_node] + 
                    self.risk_map[nei_node]
                )
                
                if temp_dist < pnt_dist[nei_node]:
                    pnt_dist[nei_node] = temp_dist

                neighb_pnts.append(nei_node)
            
            # Remove the current point from the unvisited ones
            unvisited_points.remove(curr_node)
            
            # select the unvisited node with the smallest distance
            min_dist = sys.maxsize
            
            for node in unvisited_points:
                if pnt_dist[node] < min_dist:
                
                    print(f"\t{node} = {pnt_dist[node]}")
                    min_dist = pnt_dist[node]
                    curr_node = node
            
            print(f"next current node = {curr_node}")
        
        for pnt, dist in pnt_dist.items():
            print(f"{pnt} {dist}")

    def find_all_connected_points(
            self, centre_point: tuple[int, int]) -> list[(int, int)]:
        """
        For a particular point return a list of the connected points.
        """
        
        connected_pts = []
        
        for x in range(centre_point[0]-1, centre_point[0]+2):
            for y in range(centre_point[1]-1, centre_point[1]+2):
                
                # Check to see if the point is beyond left or right hand edge
                if x < 0 or x > self.risk_map.shape[0]-1:
                    continue
                
                # Check to see if the point beyond the top or bottom edge
                if y < 0 or y > self.risk_map.shape[1]-1:
                    continue
                
                # Ignore the point itself
                if y == centre_point[1] and x == centre_point[0]:
                    continue                
                
                connected_pts.append((x, y))
        
        return connected_pts

    def find_connected_points(
            self, centre_point: tuple[int, int]) -> list[(int, int)]:
        """
        For a particular point return a list of the vertically and horizontally 
        connected points.
        """
        
        connected_pts = []
        
        if centre_point[0]-1 >= 0:
            connected_pts.append((centre_point[0]-1, centre_point[1]))
        
        if centre_point[0]+1 < self.risk_map.shape[0]:
            connected_pts.append((centre_point[0]+1, centre_point[1]))
        
        if centre_point[1]-1 >= 0:
            connected_pts.append((centre_point[0], centre_point[1]-1))
        
        if centre_point[1]+1 < self.risk_map.shape[1]:
            connected_pts.append((centre_point[0], centre_point[1]+1))
        
        return connected_pts


    def calc_path_risk(self, path_points: list[(int, int)]) -> int:
        """
        Calculate the risk score of one single path defined by a list of tuple
        integers.
        """
        pass


cavern = ChitonCave("./data/sample.txt")
cavern.find_lowest_risk_path()

