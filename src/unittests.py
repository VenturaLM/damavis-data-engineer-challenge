import unittest

from core.labyrinth import Labyrinth_solver

class TestLabyrinth(unittest.TestCase):
    """
    ### Description
    ---------------
    Labyrinth solver unittests.

    ### Example
    -------------
    >>> python3 -m unittest -v unittests.py
    """

    def test_labyrinth_columns(self):
        with self.assertRaises(ValueError) as cm:
            solver = Labyrinth_solver(path="../test/test_5.json")
            solver.solve()

            exception = cm.exception
            self.assertEqual(str(exception), f"[Labyrinth_solver] The number of rows of the labyrinth must be [3, 1000] (Current: {solver.labyrinth_shape[0] + 1}).")

    def test_labyrinth_rows(self):
        with self.assertRaises(ValueError) as cm:
            solver = Labyrinth_solver(path="../test/test_6.json")
            solver.solve()

            exception = cm.exception
            self.assertEqual(str(exception), f"[Labyrinth_solver] The number of columns of the labyrinth must be [3, 1000] (Current: {solver.labyrinth_shape[1] + 1}).")
    
    def test_check_start(self):
        with self.assertRaises(ValueError) as cm:
            solver = Labyrinth_solver(path="../test/test_7.json")
            solver.solve()

            exception = cm.exception
            self.assertEqual(str(exception), f"[Labyrinth_solver] Starting position at x coordinate out of bounds (Current: {self.start[0]} at {self.start} / Min-Max: 0-{self.labyrinth_shape[0]}).")

    def test_check_end(self):
        with self.assertRaises(ValueError) as cm:
            solver = Labyrinth_solver(path="../test/test_8.json")
            solver.solve()

            exception = cm.exception
            self.assertEqual(str(exception), f"[Labyrinth_solver] Ending position at y coordinate out of bounds (Current: {self.end[1]} at {self.end} / Min-Max: 0-{self.labyrinth_shape[1]}).")
    
    def test_1(self):
        solver = Labyrinth_solver(path="../test/test_1.json")
        solver.solve()

        self.assertEqual(solver.solution["path_length"], 11)
    
    def test_2(self):
        solver = Labyrinth_solver(path="../test/test_2.json")
        solver.solve()

        self.assertEqual(solver.solution["path_length"], -1)
    
    def test_3(self):
        solver = Labyrinth_solver(path="../test/test_3.json")
        solver.solve()

        self.assertEqual(solver.solution["path_length"], 2)
    
    def test_4(self):
        solver = Labyrinth_solver(path="../test/test_4.json")
        solver.solve()

        self.assertEqual(solver.solution["path_length"], 16)

if __name__ == '__main__':
    unittest.main()
