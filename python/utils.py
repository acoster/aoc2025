from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Sequence
import math

T = TypeVar('T')


@dataclass(eq=True, frozen=True, match_args=True, kw_only=True)
class Coord:
    """2D coordinates."""
    x: int
    y: int

    def __add__(self, other):
        return Coord(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Coord(x=self.x - other.x, y=self.y - other.y)

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __le__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y <= other.y

@dataclass(eq=True, frozen=True, match_args=True, kw_only=True)
class Coord3D:
    """3D coordinates."""
    x: int
    y: int
    z: int

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.z < other.z


    def __le__(self, other):
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.z <= other.z

    @staticmethod
    def distance(a: 'Coord3D', b: 'Coord3D') -> float:
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)

class Directions(Enum):
    NW = Coord(x=-1, y=-1)
    N = Coord(x=0, y=-1)
    NE = Coord(x=1, y=-1)
    E = Coord(x=1, y=0)
    SE = Coord(x=1, y=1)
    S = Coord(x=0, y=1)
    SW = Coord(x=-1, y=1)
    W = Coord(x=-1, y=0)


def search_in_column(matrix: Sequence[Sequence[T]], column: int, needle: T, /, start_y: int = 0) -> int:
    """
    >>> search_in_column([[1, 2, 3], [4, 5, 6]], 1, 5)
    1
    >>> search_in_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 5, start_y=2)
    -1
    """
    height = len(matrix[0])
    return next((y for y in range(start_y, height) if matrix[y][column] == needle), -1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
