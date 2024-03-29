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

The entire cave is actually five times larger in both dimensions than you 
thought; the area you originally scanned is just one tile in a 5x5 tile area 
that forms the full map. Your original map tile repeats to the right and 
downward; each time the tile repeats to the right or downward, all of its risk 
levels are 1 higher than the tile immediately up or left of it. However, risk 
levels above 9 wrap back around to 1. 

Part 1:
    What is the lowest total risk of any path from the top left to the bottom
    right?
    
Part 2:
    Using the full map, what is the lowest total risk of any path from the top 
    left to the bottom right?

"""

import numpy as np
import sys

class ChitonCave:

    def __init__(self, datafile: str):

        # Load the cave data from file and parse the risk map
        self.risk_map = np.array(
            [[int(x) for x in y] for y in
             open(datafile, "r").read().splitlines()])
        
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
            
            # For each neighbour calculate the risk
            neighb_pnts = []
            for nei_node in self.find_connected_points(curr_node):
                
                # Filter down to unvisited neighbours
                if nei_node not in unvisited_points:
                    continue
                
                # Calculate the risk for that node
                temp_dist = (
                    pnt_dist[curr_node] + 
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
                
                    min_dist = pnt_dist[node]
                    curr_node = node
        
        return pnt_dist[self.end]      
        
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
    
    def expand_the_map(self, exp_factor: int = 5):
        """
        Expand the map of the cave in both the x and y directions by the given
        `expansion_factor`.
        """
        
        orig_map = self.risk_map.copy()
        
        # Loop over the expansion factors
        outer_tmp = []
        for i in range(exp_factor):
            
            temp_arr = []
            for j in range(exp_factor):
                # Append rotated risk map
                temp_arr.append(((orig_map + i + j) % 9))
            
            # Concaternate a row of maps together
            outer_tmp.append(np.concatenate(temp_arr, axis=1))  
        
        # Create the new map by concatenating the array of concated rows
        new_map = np.concatenate(outer_tmp, axis=0)       
        
        # Replace all 0 with nines
        new_map[new_map == 0] = 9        

        # Set the new map as the main one for the class
        self.risk_map = new_map
        
        # Define the new end point
        self.end = (self.risk_map.shape[0]-1, self.risk_map.shape[1]-1)


cavern = ChitonCave("./data/input.txt")
min_risk = cavern.find_lowest_risk_path()
print(f"Part 1 Answer = {min_risk}")

cavern.expand_the_map()
min_risk = cavern.find_lowest_risk_path()
print(f"Part 2 Answer = {min_risk}")

