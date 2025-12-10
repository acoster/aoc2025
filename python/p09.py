from dataclasses import dataclass
from itertools import combinations
from typing import List
from answer import Answer
from utils import Coord


def grid_area(a: Coord, b: Coord) -> int:
    """
    >>> grid_area(Coord(x=2, y=5), Coord(x=9, y=7))
    24
    """
    return (1 + abs(a.x - b.x)) * (1 + abs(a.y - b.y))

def solve(lines: List[str]) -> Answer:
    coords : List[Coord] = []
    for l in lines:
        a, b = [int(x) for x in l.split(',')]
        coords.append(Coord(x=a, y=b))

    p1 = max([grid_area(a, b) for (a, b) in combinations(coords, 2)])

    return Answer(p1, None)

