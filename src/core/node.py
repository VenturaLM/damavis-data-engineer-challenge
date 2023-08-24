class Node:
    """
    A node class for A* Path-finding.
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # Cost of reaching next node.
        self.g = 0
        # Cost of going to next node.
        self.h = 0
        # Cheapest cost.
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
