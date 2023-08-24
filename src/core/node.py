class Node:
    """
    ### Description
    ---------------
    A node class for A* Path-finding.

    ### Parameters
    --------------
    - `parent`: parent node.
    - `position`: position within the graph.
    """

    def __init__(self, parent=None, position=None):
        # Parent node.
        self.parent = parent
        # Position within the graph.
        self.position = position
        # Rod projection.
        self.orientation = "horizontal"
        self.rod_position = self.compute_rod_position()

        # Cost of reaching next node.
        self.g = 0
        # Cost of going to next node.
        self.h = 0
        # Cheapest cost.
        self.f = 0

    def compute_rod_position(self):
        """
        ### Description
        ---------------
        Compute rod's position with the current `self.position`.

        ### Warning
        -----------
        This method assumes that the rod's shape is 3x1 (horizontal) and 1x3 (vertical).
        """
        if self.orientation == "horizontal":
            self.rod_position = [
                (self.position[0], self.position[1] - 1),
                (self.position[0], self.position[1] + 1),
            ]

        if self.orientation == "vertical":
            self.rod_position = [
                (self.position[0] - 1, self.position[1]),
                (self.position[0] + 1, self.position[1]),
            ]