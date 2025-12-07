from collections import defaultdict
from functools import cache
from typing import List, Dict, Set

from answer import Answer
from utils import Coord, search_in_column


def solve(lines: List[str]) -> Answer:
    width = len(lines[0])
    height = len(lines)
    visited: Set[Coord] = set()

    # Maps X coordinate of escaped beam to splitters that sourced it
    escaped_sources: Dict[int, List[Coord]] = defaultdict(list)
    splitter_sources: Dict[Coord, List[Coord]] = defaultdict(list)

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
            pos = search_in_column(lines, coord.x - 1, '^', start_y=coord.y)
            if pos == -1:
                escaped_sources[coord.x - 1].append(coord)
            else:
                left_splitter = Coord(x=coord.x - 1, y=pos)
                to_visit.append(left_splitter)
                splitter_sources[left_splitter].append(coord)

        if coord.x < width - 1:
            pos = search_in_column(lines, coord.x + 1, '^', start_y=coord.y)
            if pos == -1:
                escaped_sources[coord.x + 1].append(coord)
            else:
                right_splitter = Coord(x=coord.x + 1, y=pos)
                to_visit.append(right_splitter)
                splitter_sources[right_splitter].append(coord)

    @cache
    def count_timelines(c: Coord):
        if c not in splitter_sources:
            return 1
        return sum([count_timelines(s) for s in splitter_sources[c]])

    timelines = 0
    for x, sources in escaped_sources.items():
        for splitter in sources:
            timelines += count_timelines(splitter)

    return Answer(splits, timelines)
