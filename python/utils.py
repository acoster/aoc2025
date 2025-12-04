from dataclasses import dataclass
from enum import Enum

@dataclass(eq=True, frozen=True)
class Coord:
    """2D coordinates."""
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)


class Directions(Enum):
    UP_LEFT = Coord(-1, -1)
    UP = Coord(0, -1)
    UP_RIGHT = Coord(1, -1)

    LEFT = Coord(-1, 0)
    RIGHT = Coord(1, 0)

    DOWN_LEFT = Coord(-1, 1)
    DOWN = Coord(0, 1)
    DOWN_RIGHT = Coord(1, 1)