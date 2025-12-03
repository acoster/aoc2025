import re
from typing import List

from answer import Answer


def solve_range(id_range: str) -> Answer:
    """
    >>> solve_range('998-1012')
    Answer(part_one=1010, part_two=2009)
    >>> solve_range('1188511880-1188511890')
    Answer(part_one=1188511885, part_two=1188511885)
    """
    assert id_range.count('-') == 1
    lower_bound, upper_bound = [int(x) for x in id_range.split('-')]
    prog = re.compile(r"^([0-9]+)(\1)(\1)*$")

    extended_total = 0
    simple_total = 0

    for i in range(lower_bound, upper_bound + 1):
        match = prog.match(str(i))
        if match is None:
            continue

        if match.group(3) is None:
            simple_total += i
        extended_total += i

    return Answer(simple_total, extended_total)


def solve(lines: List[str]):
    assert len(lines) == 1
    result = Answer(0, 0)

    for id_range in lines[0].split(','):
        result += solve_range(id_range)

    return result
