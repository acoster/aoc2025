from collections import defaultdict
from typing import List

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
    def __init__(self):
        self.neighbour_count = defaultdict(int)
        self.rolls = set()

    def add_roll(self, coord: Coord):
        self.rolls.add(coord)
        for direction in Directions:
            self.neighbour_count[coord + direction.value] += 1

    def new_generation(self) -> int:
        previous_rolls = self.rolls.copy()
        previous_count = self.neighbour_count.copy()
        self.neighbour_count = defaultdict(int)
        self.rolls = set()

        removed = 0
        for coord in previous_rolls:
            if previous_count[coord] < 4:
                removed += 1
            else:
                self.add_roll(coord)

        return removed


def solve(lines: List[str]) -> Answer:
    """
    >>> solve(_test_input())
    Answer(part_one=13, part_two=43)
    """
    grid = Grid()

    for y in range(len(lines)):
        row = lines[y]
        for x in range(len(row)):
            if row[x] == '@':
                grid.add_roll(Coord(x, y))

    part_one = grid.new_generation()
    part_two = part_one
    while True:
        removed = grid.new_generation()
        if removed == 0:
            break
        part_two += removed

    return Answer(part_one, part_two)
