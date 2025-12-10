from itertools import combinations
from typing import List
from answer import Answer
from utils import Coord

from shapely.geometry import Polygon


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

    polygon = Polygon((a.x, a.y) for a in coords)

    p1 = 0
    p2 = 0
    for a, b in combinations(coords, 2):
        area = grid_area(a, b)
        p1 = max(p1, area)

        sq = Polygon([[a.x, a.y], [b.x, a.y], [b.x, b.y], [a.x, b.y]])
        if polygon.covers(sq):
            p2 = max(p2, area)

    return Answer(p1, p2)

