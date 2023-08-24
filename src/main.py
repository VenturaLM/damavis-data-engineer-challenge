import argparse

from core.labyrinth import Labyrinth_solver


def main():
    """
    ### Description
    ---------------
    Main script to run the Labyrinth solver.

    ### Example
    -----------
    >>> python3 main.py -L ../test/test_3.json ../test/test_4.json ../test/test_2.json
    """
    # Command line argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-L", "--labyrinth_path", nargs="+", type=str, help="Path of the labyrinth(s) data. It takes 1 or more paths", required=True
    )

    args = parser.parse_args()
    
    # Run each file in passed in `args.labyrinth_path`.
    for file in args.labyrinth_path:
        print(f"\nFile {file}:")
        print("===========================")
        solver = Labyrinth_solver(path=file)
        solver.solve()
        print(solver.solution)


if __name__ == "__main__":
    main()
