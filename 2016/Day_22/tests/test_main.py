"""
Tests for the main script
"""

from main import NodeGrid


def test_data_parse():
    test = NodeGrid("./data/example_01.txt")
    assert test.nodes == [
        {"Node": "/dev/grid/node-x0-y19", "Size": 92, "Used": 66, "Avail": 26},
        {"Node": "/dev/grid/node-x0-y20", "Size": 94, "Used": 69, "Avail": 25},
        {"Node": "/dev/grid/node-x0-y21", "Size": 88, "Used": 65, "Avail": 23},
        {"Node": "/dev/grid/node-x0-y22", "Size": 87, "Used": 72, "Avail": 15},
        {"Node": "/dev/grid/node-x0-y23", "Size": 92, "Used": 66, "Avail": 26},
        {"Node": "/dev/grid/node-x0-y24", "Size": 89, "Used": 72, "Avail": 17},
        {"Node": "/dev/grid/node-x1-y0", "Size": 86, "Used": 66, "Avail": 20},
        {"Node": "/dev/grid/node-x1-y1", "Size": 93, "Used": 64, "Avail": 29},
        {"Node": "/dev/grid/node-x1-y2", "Size": 92, "Used": 65, "Avail": 27},
        {"Node": "/dev/grid/node-x1-y3", "Size": 92, "Used": 70, "Avail": 22},
        {"Node": "/dev/grid/node-x1-y4", "Size": 87, "Used": 72, "Avail": 15},
        {"Node": "/dev/grid/node-x1-y5", "Size": 87, "Used": 69, "Avail": 18},
        {"Node": "/dev/grid/node-x7-y17", "Size": 92, "Used": 0, "Avail": 92},
    ]


def test_find_viable_pairs():
    assert len(NodeGrid("./data/example_01.txt").viable_pairs()) == 12
