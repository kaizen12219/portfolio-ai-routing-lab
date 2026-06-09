from collections import deque
from dataclasses import dataclass
from heapq import heappop, heappush

from .grid import Grid, Point


@dataclass(frozen=True)
class RouteResult:
    algorithm: str
    path: tuple[Point, ...]
    visited_count: int

    @property
    def found(self) -> bool:
        return bool(self.path)

    @property
    def steps(self) -> int:
        return max(0, len(self.path) - 1)


def breadth_first(grid: Grid, start: Point, goal: Point) -> RouteResult:
    frontier: deque[Point] = deque([start])
    came_from: dict[Point, Point | None] = {start: None}

    while frontier:
        current = frontier.popleft()
        if current == goal:
            break
        for neighbor in grid.neighbors(current):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current

    return RouteResult("breadth-first", _reconstruct(came_from, start, goal), len(came_from))


def astar(grid: Grid, start: Point, goal: Point) -> RouteResult:
    frontier: list[tuple[int, Point]] = []
    heappush(frontier, (0, start))
    came_from: dict[Point, Point | None] = {start: None}
    cost_so_far: dict[Point, int] = {start: 0}

    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            break
        for neighbor in grid.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + _manhattan(neighbor, goal)
                heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return RouteResult("a-star", _reconstruct(came_from, start, goal), len(came_from))


def _reconstruct(came_from: dict[Point, Point | None], start: Point, goal: Point) -> tuple[Point, ...]:
    if goal not in came_from:
        return tuple()

    current: Point | None = goal
    path: list[Point] = []
    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return tuple(path) if path and path[0] == start else tuple()


def _manhattan(left: Point, right: Point) -> int:
    return abs(left.x - right.x) + abs(left.y - right.y)
