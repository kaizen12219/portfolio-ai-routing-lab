from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Grid:
    width: int
    height: int
    blocked: frozenset[Point] = frozenset()

    def contains(self, point: Point) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def passable(self, point: Point) -> bool:
        return point not in self.blocked

    def neighbors(self, point: Point) -> list[Point]:
        candidates = [
            Point(point.x + 1, point.y),
            Point(point.x - 1, point.y),
            Point(point.x, point.y + 1),
            Point(point.x, point.y - 1),
        ]
        return [item for item in candidates if self.contains(item) and self.passable(item)]
