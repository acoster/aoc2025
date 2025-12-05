from typing import List

from answer import Answer
from utils import Interval


def solve(lines: List[str]) -> Answer:
    i = 0
    intervals = []
    valid_ids = 0

    while i < len(lines):
        if '-' not in lines[i]:
            i += 1
            break
        a, b = [int(x) for x in lines[i].split('-')]
        intervals.append(Interval(a, b))
        i += 1

    for product_id in lines[i:]:
        if any([int(product_id) in y for y in intervals]):
            valid_ids += 1

    return Answer(valid_ids, None)
