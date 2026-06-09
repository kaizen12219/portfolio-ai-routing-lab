import argparse
import json

from .grid import Grid, Point
from .router import astar, breadth_first
from .scoring import score_route


def main() -> None:
    parser = argparse.ArgumentParser(description="Explain a route through a blocked grid.")
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--blocked", nargs="*", default=[])
    parser.add_argument("--algorithm", choices=["astar", "breadth-first"], default="astar")
    args = parser.parse_args()

    grid = Grid(args.width, args.height, frozenset(_parse_point(item) for item in args.blocked))
    start = _parse_point(args.start)
    goal = _parse_point(args.goal)
    result = astar(grid, start, goal) if args.algorithm == "astar" else breadth_first(grid, start, goal)

    print(json.dumps({
        "summary": score_route(result),
        "path": [point.__dict__ for point in result.path],
    }, indent=2))


def _parse_point(value: str) -> Point:
    x, y = value.split(",", maxsplit=1)
    return Point(int(x), int(y))


if __name__ == "__main__":
    main()
