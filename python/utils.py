from dataclasses import dataclass
from enum import Enum


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

@dataclass(eq=True, frozen=True, match_args=True)
class Interval:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        assert a <= b
        object.__setattr__(self, 'a', a)
        object.__setattr__(self, 'b', b)

    def __contains__(self, other: int):
        """
        >>> 3 in Interval(3, 4)
        True
        """
        return self.a <= other <= self.b

    def __lt__(self, other):
        if self.a != other.a:
            return self.a < other.a
        return self.b < other.b

    def __le__(self, other):
        if self.a != other.a:
            return self.a < other.a
        return self.b <= other.b

class Directions(Enum):
    NW = Coord(x=-1, y=-1)
    N = Coord(x=0, y=-1)
    NE = Coord(x=1, y=-1)
    E = Coord(x=1, y=0)
    SE = Coord(x=1, y=1)
    S = Coord(x=0, y=1)
    SW = Coord(x=-1, y=1)
    W = Coord(x=-1, y=0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()