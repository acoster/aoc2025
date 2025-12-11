from collections import defaultdict
from functools import cache
from typing import List

from answer import Answer

G = defaultdict(set)


@cache
def count_paths(src: str, dst: str) -> int:
    if src == dst:
        return 0
    if dst in G[src]:
        return 1
    return sum((count_paths(h, dst) for h in G[src]))


def solve(lines: List[str]) -> Answer:
    for l in lines:
        src, connections = l.split(': ')
        for c in connections.split():
            G[src].add(c)

    p0 = count_paths('you', 'out')
    p1 = (count_paths('svr', 'fft') * count_paths('fft', 'dac') *
          count_paths('dac', 'out'))
    p1 += (count_paths('svr', 'dac') * count_paths('dac', 'fft') *
           count_paths('fft', 'out'))

    return Answer(p0, p1)
