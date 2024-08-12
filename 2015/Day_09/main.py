"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a
single night.

This year, however, he has some new locations to visit; his
elves have provided him the distances between every pair of
locations. He can start and end at any two (different)
locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve
this?

PART 1: What is the distance of the shortest route?
"""

import networkx
import matplotlib.pyplot as plt


class DeliveryNetwork:

    def __init__(self, data_file: str):
        """
        The locations and routes that Santa visits when
        delivering presents in a single night.
        """
        self.dn = networkx.Graph()

        # Create the graph from the data file
        with open(data_file) as fp:
            for line in fp:

                # Extract the data
                route, dist = line.split(" = ")
                loc_a, loc_b = route.split(" to ")

                # Add the nodes
                self.dn.add_node(loc_a)
                self.dn.add_node(loc_b)

                # Add the edge between them
                self.dn.add_edge(loc_a, loc_b, length=int(dist))

                # self.dn = add_edge_from((loc_a, loc_b, {"w": int(dist)}))

    def sv_image(self, img_file: str):
        """
        Save an image of Santas delivery network to disk.
        """
        node_postions = networkx.spring_layout(self.dn)
        node_sizes = [len(x) * 800 for x in self.dn.nodes()]

        plt.figure(3, figsize=(12, 12))
        networkx.draw(self.dn, node_postions, with_labels=True, node_size=node_sizes)

        # Add the distances to the lables
        edge_labels = dict(
            [
                (
                    (
                        u,
                        v,
                    ),
                    d["length"],
                )
                for u, v, d in self.dn.edges(data=True)
            ]
        )
        networkx.draw_networkx_edge_labels(
            self.dn, node_postions, edge_labels=edge_labels, font_color="black"
        )

        plt.savefig(img_file)


if __name__ == "__main__":
    xmas_route = DeliveryNetwork("./data/input.txt")
    xmas_route.sv_image("./graphs/input_routes.png")
