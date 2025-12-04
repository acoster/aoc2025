from typing import List
from collections import defaultdict

from answer import Answer
from utils import Coord, Directions


def _test_input():
    s = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''
    return [l.strip() for l in s.split('\n')]

class Grid:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.neighbour_count  = defaultdict(int)
        self.rolls = set()


    def add_roll(self, coord: Coord):
        self.rolls.add(coord)
        for direction in Directions:
            self.neighbour_count[coord + direction.value] += 1



def solve(lines: List[str]) -> Answer:
    """
    >>> solve(_test_input())
    Answer(part_one=13, part_two=None)
    """
    grid = Grid(len(lines[0]), len(lines))

    for y in range(len(lines)):
        row = lines[y]
        for x in range(len(row)):
            if row[x] == '@':
                grid.add_roll(Coord(x, y))


    part_one = 0
    for r in grid.rolls:
        if grid.neighbour_count[r] < 4:
            part_one += 1

    return Answer(part_one, None)
