import re
from typing import List
from collections import namedtuple

from absl import flags, app

FLAGS = flags.FLAGS
flags.DEFINE_string('input', '', 'Path to input file.')

RangeResult = namedtuple('Result', ['simple_rule', 'extended_rules'])

def solve_range(id_range: str) -> RangeResult:
    """
    >>> solve_range('998-1012')
    Result(simple_rule=1010, extended_rules=2009)
    >>> solve_range('1188511880-1188511890')
    Result(simple_rule=1188511885, extended_rules=1188511885)
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

    return RangeResult(simple_total, extended_total)


def main(argv: List[str]) -> int:
    import doctest
    doctest.testmod()

    if FLAGS.input != '':
        total = 0
        extended_total = 0
        with open(FLAGS.input) as f:
            data = f.readline().strip()
            for id_range in data.split(','):
                result = solve_range(id_range)
                total += result.simple_rule
                extended_total += result.extended_rules
        print(
            f'Results: {total}, {extended_total}')
    return 0


if __name__ == '__main__':
    app.run(main)
