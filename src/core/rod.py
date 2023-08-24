class Rod:
    """
    Class representing a rod.
    """

    def __init__(self) -> None:
        # Possible adjacent squares.
        self.movements = [
            (0, 1),  # Up
            (0, -1),  # Down
            (1, 0),  # Right
            (-1, 0),  # Left
        ]
        self.shape = (3, 1)
        self.position = (0, 0)
        self.orientation = "horizontal"
