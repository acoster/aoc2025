from typing import List

from answer import Answer
from utils import Coord


def solve(lines: List[str]) -> Answer:
    width = len(lines[0])
    height = len(lines)
    visited = set()


    src = lines[0].find('S')
    assert src != -1

    first_splitter = ''.join(lines[y][src] for y in range(height)).find('^')
    assert first_splitter != -1

    splits = 0
    to_visit = [Coord(x=src, y=first_splitter)]
    while len(to_visit) > 0:
        coord = to_visit.pop()
        if coord in visited:
            continue
        visited.add(coord)
        splits += 1

        if coord.x > 0:
            left_splitter = ''.join(lines[y][coord.x - 1] for y in range(coord.y, height)).find('^')
            if left_splitter != -1:
                to_visit.append(Coord(x=coord.x - 1, y=coord.y + left_splitter))

        if coord.x < width - 1:
            right_splitter = ''.join(lines[y][coord.x + 1] for y in range(coord.y, height)).find('^')
            if right_splitter != -1:
                to_visit.append(Coord(x=coord.x + 1, y=coord.y + right_splitter))

    return Answer(splits, None)
