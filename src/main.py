from core.labyrinth import Labyrinth_solver


def main():
    """
    ### Description
    ---------------
    Main script to run the Labyrinth solver.
    """

    # for i in range(1, 5):
    # print(f"\nTest {i}:")
    solver = Labyrinth_solver(path=f"test/test_{1}.txt")
    solver.solve()
    solver.print_solution()


if __name__ == "__main__":
    main()
