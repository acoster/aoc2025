from typing import List

import portion

from answer import Answer


def solve(lines: List[str]) -> Answer:
    i = 0
    valid_ids = 0

    ranges = portion.empty()

    while i < len(lines):
        if '-' not in lines[i]:
            i += 1
            break
        a, b = [int(x) for x in lines[i].split('-')]
        ranges = ranges | portion.closed(a, b)
        i += 1

    total_valid_ids = 0
    for id_range in ranges:
        total_valid_ids += id_range.upper - id_range.lower + 1

    for product_id in lines[i:]:
        if int(product_id) in ranges:
            valid_ids += 1

    return Answer(valid_ids, total_valid_ids)
