import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from portfolio_ai_routing import Grid, Point, astar, breadth_first, score_route


class RouterTests(unittest.TestCase):
    def test_astar_routes_around_blocked_column(self) -> None:
        grid = Grid(6, 5, frozenset({Point(2, 1), Point(2, 2), Point(2, 3)}))
        result = astar(grid, Point(0, 0), Point(5, 4))

        self.assertTrue(result.found)
        self.assertEqual(result.path[0], Point(0, 0))
        self.assertEqual(result.path[-1], Point(5, 4))
        self.assertNotIn(Point(2, 2), result.path)

    def test_breadth_first_reports_missing_path(self) -> None:
        grid = Grid(3, 3, frozenset({Point(1, 0), Point(1, 1), Point(1, 2)}))
        result = breadth_first(grid, Point(0, 1), Point(2, 1))

        self.assertFalse(result.found)
        self.assertEqual(score_route(result)["score"], 0)

    def test_route_score_rewards_found_paths(self) -> None:
        grid = Grid(4, 4)
        result = astar(grid, Point(0, 0), Point(3, 3))

        self.assertGreater(score_route(result)["score"], 50)


if __name__ == "__main__":
    unittest.main()
