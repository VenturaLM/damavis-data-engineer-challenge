import json

from core.node import Node


class Labyrinth_solver:
    """
    ### Description
    ---------------
    Class representing a labyrinth solver.

    ### Parameters
    --------------
    - `path`: labyrinth file path.
    """

    def __init__(self, path: str) -> None:
        # Labyrinth matrix.
        self.labyrinth = None
        # Labyrinth shape.
        self.labyrinth_shape = None
        # Starting point.
        self.start = None
        # Ending point.
        self.end = None
        # The rod can only be rotated about its center, and only if the 3 x 3 area surrounding it is
        # clear from the obstacles or the walls.
        self.obstacle_constraint = (3, 3)
        # Solution.
        self.solution = dict()

        # Read labyrinth from file.
        self._read_labyrinth(path=path)

    def _check_labyrinth(self) -> None:
        """ 
        ### Description
        ---------------
        Method that checks:
        1. The labyrinth is a `list` instance.
        2. The number of rows is in [3, 1000] range.
        3. The number of columns is in [3, 1000] range.

        ### Raises
        ----------
        - `TypeError`: if `self.labyrinth` is not a `list` instance.
        - `ValueError`: either number of rows or columns is not in range.
        """
        # Check if `labyrinth` belongs to a valid class.
        if not isinstance(self.labyrinth, list):
            raise TypeError(
                f"[Labyrinth_solver] Inappropriate argument type in 'labyrinth' while initializing labyrinth: {type(self.labyrinth)}."
            )

        self.labyrinth_shape = (len(self.labyrinth) - 1, len(self.labyrinth[0]) - 1)

        if not 2 <= self.labyrinth_shape[0] <= 999:
            raise ValueError(
                f"[Labyrinth_solver] The number of rows of the labyrinth must be [3, 1000] (Current {self.labyrinth_shape[0] + 1})."
            )
        if not 2 <= self.labyrinth_shape[1] <= 999:
            raise ValueError(
                f"[Labyrinth_solver] The number of columns of the labyrinth must be [3, 1000] (Current {self.labyrinth_shape[1] + 1})."
            )

    def _check_start(self) -> None:
        """
        ### Description
        ---------------
        Method that checks that the starting point type is a tuple instance.

        ### Raises
        ----------
        - `TypeError`: if `self.start` is not a `tuple` instance.
        """
        if not isinstance(self.start, tuple):
            raise TypeError(
                f"[Labyrinth_solver] Inappropriate argument type in 'start' while initializing labyrinth: {type(self.start)}."
            )

    def _check_end(self) -> None:
        """
        ### Description
        ---------------
        Method that checks that the ending point type is a tuple instance.

        ### Raises
        ----------
        - `TypeError`: if `self.end` is not a `tuple` instance.
        """
        if not isinstance(self.end, tuple):
            raise TypeError(
                f"[Labyrinth_solver] Inappropriate argument type in 'end' while initializing labyrinth: {type(self.end)}."
            )

    def _read_labyrinth(self, path: str) -> None:
        """
        ### Description
        ---------------
        Read a labyrinth given a '.txt' file stored at `path`.

        ### Parameters
        --------------
        - `path`: labyrinth file path.
        """
        # Read file content.
        with open(path, "r") as file:
            content = json.load(file)

        try:
            self.labyrinth = eval(content["labyrinth"])
            self._check_labyrinth()
        except Exception as e:
            raise e

        self.start = eval(content["start"])
        self._check_start()

        self.end = eval(content["end"])
        self._check_end()

    def is_within_labyrinth(self, x: int, y: int) -> bool:
        """
        ### Description
        ---------------
        Checks wether a move is within the labyrinth or not.

        ### Parameters
        --------------
        - `x`: coordinate x.
        - `y`: coordinate y.
        """
        if 0 <= x <= self.labyrinth_shape[0] and 0 <= y <= self.labyrinth_shape[1]  and self.labyrinth[x][y] == ".":
            return True

        return False
    
    def is_valid_move(self, node: Node, x: int, y: int) -> bool:
        """

        """        
        if node.orientation == "horizontal":
            if y - 1 >= 0 and y + 1 <= self.labyrinth_shape[1]:
                if self.labyrinth[x][y - 1] == "." and self.labyrinth[x][y + 1] == ".":
                    return True
        if node.orientation == "vertical":
            if x - 1 >= 0 and x + 1 <= self.labyrinth_shape[0]:
                if self.labyrinth[x - 1][y] == "." and self.labyrinth[x + 1][y] == ".":
                    return True

        return False

    def is_valid_rotation(self, x: int, y: int, orientation: str) -> bool:
        """
        ### Description
        ---------------
        Checks wether a rotation is valid or not given a current context (space and orientation) and
        certain constraints given by `obstacle_constraint`.

        ### Parameters
        --------------
        - `x`: coordinate x.
        - `y`: coordinate y.
        - `orientation`: current rod orientation.
        """
        if orientation == "horizontal":
            # For the given constraint.
            for i in range(
                x - self.obstacle_constraint[0] + 2, x + self.obstacle_constraint[0] - 2
            ):
                for j in range(
                    y - self.obstacle_constraint[0] + 2,
                    y + self.obstacle_constraint[0] - 2,
                ):
                    # Check that the new position is valid given the labyrinth shape and the blocked
                    # spots.
                    if (
                        0 <= i < self.labyrinth_shape[0]
                        and 0 <= j < self.labyrinth_shape[1]
                        and self.labyrinth[i][j] == "#"
                    ):
                        return False
        else:
            # For the given constraint.
            for i in range(
                x - self.obstacle_constraint[0] + 2, x + self.obstacle_constraint[0] - 2
            ):
                for j in range(
                    y - self.obstacle_constraint[0] + 2,
                    y + self.obstacle_constraint[0] - 2,
                ):
                    # Check that the new position is valid given the labyrinth shape and the blocked
                    # spots.
                    if (
                        0 <= i < self.labyrinth_shape[0]
                        and 0 <= j < self.labyrinth_shape[1]
                        and self.labyrinth[i][j] == "#"
                    ):
                        return False
        return True

    def a_star(self):
        """
        ### Description
        ---------------
        Method that solves the labyrinth using A* Path-finding algorithm.

        ### Returns
        -----------
        List of tuples as a path from the given start to the given end in the given labyrinth.
        """
        # Start node.
        start_node = Node(parent=None, position=self.start)
        start_node.g = start_node.h = start_node.f = 0

        # End node.
        end_node = Node(parent=None, position=self.end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list.
        open_list = list()  # Options to visit.
        closed_list = list()  # Options visited.

        # Add the start node.
        open_list.append(start_node)

        # Loop until finding the end.
        while len(open_list) > 0:
            # Get the current node.
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

                    # Check rod constraints.
                    if current_node.orientation == "horizontal":
                        if self.is_valid_rotation(
                            x=current_node.position[0], 
                            y=current_node.position[1], 
                            orientation="vertical"
                        ):
                            current_node.orientation = "vertical"
                    else:
                        if self.is_valid_rotation(
                            x=current_node.position[0], 
                            y=current_node.position[1], 
                            orientation="horizontal"
                        ):
                            current_node.orientation = "horizontal"

                current_node.compute_rod_position()

            # Pop current off open list, add to closed list.
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal.
            if end_node.position in current_node.rod_position:
                path = []
                current = current_node
                while current is not None:
                    path.append((current.position, current.orientation))
                    current = current.parent
                return path[::-1]  # Return reversed path.

            # Generate children.
            children = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Movements.
                # Get node position.
                node_position = (
                    current_node.position[0] + dx,
                    current_node.position[1] + dy,
                )

                # Checks.
                if self.is_within_labyrinth(x=node_position[0], y=node_position[1]) == False:
                    continue
                if self.is_valid_move(node=current_node, x=node_position[0], y=node_position[1]) == False:
                    continue

                # Create new node.
                new_node = Node(current_node, node_position)

                # Append.
                children.append(new_node)

            # Loop through children.
            for child in children:
                # Child is on the closed list.
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values.
                # ------------------------------
                # Cost of reaching next node.
                child.g = current_node.g + 1
                # Manhattan distance.
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2
                )
                # Cost f(n) = g(n) + h(n).
                child.f = child.g + child.h

                # Child is already in the open list.
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list.
                open_list.append(child)

    def solve(self) -> int:
        """
        ### Description
        ---------------
        Core method to solve the labyrinth.
        """
        path = self.a_star()
        path_length = -1 if path is None else len(path)

        self.solution["path"] = path
        self.solution["path_length"] = path_length - 1 # Subtract the first move (0, 0).
