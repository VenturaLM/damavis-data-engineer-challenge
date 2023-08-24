from core.node import Node
from core.rod import Rod


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
        # Rod instance.
        self.rod = Rod()
        # The rod can only be rotated about its center, and only if the 3 x 3 area surrounding it is
        # clear from the obstacles or the walls.
        self.obstacle_constraint = (3, 3)
        # Solution.
        self.solution = dict()

        # Read labyrinth from file.
        self._read_labyrinth(path=path)

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
            content = file.read()

        # Evaluate expression of `content` as python code.
        labyrinth = eval(content)

        # Check if `labyrinth` belong to a valid class.
        if isinstance(labyrinth, list):
            self.labyrinth = eval(content)
            self.labyrinth_shape = (len(self.labyrinth) - 1, len(self.labyrinth[0]) - 1)
        else:
            raise TypeError(
                f"[Labyrinth_solver] Inappropriate argument type while initializing labyrinth: {type(labyrinth)}."
            )

    def is_valid_move(self, x: int, y: int) -> bool:
        """
        ### Description
        ---------------
        Checks wether a move is valid within the labyrinth or not.

        ### Parameters
        --------------
        - `x`: coordinate x.
        - `y`: coordinate y.
        """
        if (
            0 <= x <= self.labyrinth_shape[0]
            and 0 <= y <= self.labyrinth_shape[1]
            and self.labyrinth[x][y] == "."
        ):
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

    def a_star(self, start: set, end: set):
        """
        ### Description
        ---------------
        Method that solves the labyrinth using A* Path-finding algorithm.

        ### Parameters
        --------------
        - `start`: starting point.
        - `end`: ending point.

        ### Returns
        -----------
        List of tuples as a path from the given start to the given end in the given labyrinth.
        """
        # Start node.
        start_node = Node(parent=None, position=start)
        start_node.g = start_node.h = start_node.f = 0

        # End node.
        end_node = Node(parent=None, position=end)
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
                    self.rod.position = current_node.position

            # Pop current off open list, add to closed list.
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal.
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path.

            # Generate children.
            children = []
            for dx, dy in self.rod.movements:
                # Get node position.
                node_position = (
                    current_node.position[0] + dx,
                    current_node.position[1] + dy,
                )

                # ==================================================================================
                # Checks.
                if self.is_valid_move(x=node_position[0], y=node_position[1]) == False:
                    continue

                # if (
                #     self.is_valid_rotation(
                #         x=node_position[0],
                #         y=node_position[1],
                #         orientation=self.rod.orientation,
                #     )
                #     == False
                # ):
                #     continue
                # ==================================================================================

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
                ...

    def print_solution(self):
        """
        ### Description
        ---------------
        Prints the solution to the labyrinth problem passed as argument firstly with the following
        structure:

        >>> solution = {'path': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (1, 6), (2, 6), (2, 7), (2, 8), (3, 8), (4, 8)], 'path_length': 13}
        """
        print(f"Solution:")
        print(f"=========")
        print(f"{self.solution}")

    def solve(self) -> int:
        """
        ### Description
        ---------------
        Core method to solve the labyrinth.
        """
        path = self.a_star(start=(0, 0), end=(4, 8))
        path_length = len(path)

        self.solution["path"] = path
        self.solution["path_length"] = path_length
