"""
--- Day 13: Packet Scanners ---

You need to cross a vast firewall. The firewall consists of several layers,
each with a security scanner that moves back and forth across the layer. To
succeed, you must not be detected by a scanner.

Within each layer, a security scanner moves back and forth within its range.
Each security scanner starts at the top and moves down until it reaches the
bottom, then moves up until it reaches the top, and repeats.

A security scanner takes one picosecond to move one step.

The plan is to hitch a ride on a packet about to move through the firewall.
The packet will travel along the top of each layer, and it moves at one layer
per picosecond.

Each picosecond, the packet moves one layer forward (its first move takes it
into layer 0), and then the scanners move one step.

If there is a scanner at the top of the layer as your packet enters it, you are
caught. (If a scanner moves into the top of its layer while you are there, you
are not caught.
"""


class Firewall:

    def __init__(self, firewall_scheme_fp):

        self.packet_pos = -1
        self.severity = 0

        # Load the firewall scheme from disk
        scheme = {}
        with open(firewall_scheme_fp, "r") as file:
            for line in file:
                raw = line.split(": ")
                scheme[int(raw[0])] = int(raw[1].strip())

        # Construct the firewall as empty lists representing the layers
        self.layers = [{
            "depth": scheme.get(x, 0),
            "scanner_pos": None,
            "scanner_direction": -1
                        } for x in range(max(scheme) + 1)]

    def initialise_scanners(self):
        """Set the scanners to the top of the levels."""

        for fire_layer in self.layers:
            if fire_layer["depth"] > 0:
                fire_layer["scanner_pos"] = 0

    def move_scanners(self):
        """Move the scanners to their next position."""

        for fire_layer in self.layers:
            if fire_layer["scanner_pos"] is not None:

                if fire_layer["scanner_pos"] <= 0 or \
                        fire_layer["scanner_pos"] >= fire_layer["depth"]-1:
                    fire_layer["scanner_direction"] *= -1

                fire_layer["scanner_pos"] += fire_layer["scanner_direction"]

    def move_packet(self):
        """Move the packet along the top of the layers."""
        self.packet_pos += 1

    def time_step(self):
        """Simulate a timestep of the packet traversing the firewall"""

        self.move_packet()

        if self.is_packet_caught():
            self.severity += self.calc_severity_score()

        self.move_scanners()

    def is_packet_caught(self) -> bool:
        """
        Has the packet been caught by the scanners? Is it in the same square as
        a scanner?
        """
        return self.layers[self.packet_pos]["scanner_pos"] == 0

    def calc_severity_score(self) -> int:
        """
        What is the severity score if the packet was discovered in its current
        position?
        """
        return self.layers[self.packet_pos]["depth"] * self.packet_pos

    def traverse_firewall(self, delay=0) -> int:
        """
        Move the package across the firewall and return the total severity
        from the crossing. Delay means letting the scanners move delay number
        of cycles before the packet starts moving.
        """

        self.initialise_scanners()

        for _ in range(delay):
            self.move_scanners()

        while self.packet_pos < len(self.layers)-1:
            self.time_step()

            if delay > 0 and self.severity > 0:
                break

        return self.severity

    def clear_path(self, delay) -> bool:
        """
        Determine if a delay of a certain time would mean the packet
        wouldn't get caught.
        """

        # Set up the firewall scanners, and packets
        self.initialise_scanners()

        for _ in range(delay):
            self.move_scanners()

        # Move the packet
        while self.packet_pos < len(self.layers) - 1:

            self.move_packet()

            if self.is_packet_caught():
                return False

            self.move_scanners()

        else:
            return True


# Part 1
basic_crossing = Firewall("data/input.txt")
print(basic_crossing.traverse_firewall())

