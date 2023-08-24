# Problem definition
The goal is to carry the rod from the top left corner of the labyrinth to the bottom
right corner. This rod is not exactly the lightest thing you can imagine, so the participant would naturally want to do it as fast as possible.

Find the minimal number of moves required to carry the rod through the labyrinth.
The labyrinth can be represented as a rectangular matrix, some cells of which are
marked as blocked, and the rod can be represented as a 1 × 3 rectangle. The rod can't collide with the blocked cells or the walls, so it's impossible to move it into a position in which one of its cells coincides with the blocked cell or the wall. The goal is thus to move the rod into position in which one of its cells is in the bottom right cell of the labyrinth.

There are 5 types of moves that the participant can perform: move the rod one cell
down or up, to the right or to the left, or to change its orientation from vertical to horizontal and vice versa. The rod can only be rotated about its center, and only if the $3 \times 3$ area surrounding it is clear from the obstacles or the walls.

The rod is initially positioned horizontally, and its left cell lies in $[0, 0]$.

### Labyrinth graphical example [1]
![Labyrinth example](image/labyrinth_example.png)

### Labyrinth codification example
    labyrinth = [
        [".",".",".",".",".",".",".",".","."],
        ["#",".",".",".","#",".",".",".","."],
        [".",".",".",".","#",".",".",".","."],
        [".","#",".",".",".",".",".","#","."],
        [".","#",".",".",".",".",".","#","."]
    ]

The result in this example is 11.

# A* approach
The strategy followed for solving the problem has been an A* search approach [2]. It evaluates nodes by combining $g(n)$, the cost to reach the node, and $h(n)$, the cost to reach the goal node:

$f(n) = g(n) + h(n)$

Since $g(n)$ gives us the cost of the path from the start node to node $n$, and $h(n)$ gives us the estimated cost of the cheapest path from $n$ to the goal, we have:
$f(n)$ = estimated cheapest cost of the solution through $n$.
Thus, if we try to find the cheapest solution, it is reasonable to first consider the node with the lowest value of $g(n) + h(n)$. It turns out that this strategy is more than reasonable: as long as the heuristic function $h(n)$ satisfies certain conditions, the A* search is both complete and optimal.

# References
[1]: [Damavis studio](https://damavis.com/en/).

[2]: Russell, Stuart J. and Norvig, Peter. (2010). Artificial Intelligence: A modern approach. Prentice-Hall.