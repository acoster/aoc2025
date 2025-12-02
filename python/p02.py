import re
from typing import Iterator, List

from absl import flags, app

FLAGS = flags.FLAGS

flags.DEFINE_string('input', '', 'Path to input file.')

def generate_sequence(id_range: str, extended_rules: bool = False) -> Iterator[
    int]:
    """
    >>> [x for x in generate_sequence('11-22')]
    [11, 22]
    >>> [x for x in generate_sequence('1188511880-1188511890', True)]
    [1188511885]
    >>> [x for x in generate_sequence('95-115', True)]
    [99, 111]
    """
    assert id_range.count('-') == 1
    lower_bound, upper_bound = [int(x) for x in id_range.split('-')]
    prog = re.compile(r"^([0-9]+)(\1)+$")

    for i in range(lower_bound, upper_bound + 1):
        value = str(i)
        length = len(value)

        if extended_rules:
            if prog.fullmatch(value):
                yield i
        elif length % 2 == 0 and value[0:length // 2] == value[-(length // 2):]:
            yield i


def main(argv: List[str]) -> int:
    import doctest
    doctest.testmod(raise_on_error=True)

    if FLAGS.input != '':
        total = 0
        extended_total = 0
        with open(FLAGS.input) as f:
            data = f.readline().strip()
            for id_range in data.split(','):
                total += sum(generate_sequence(id_range))
                extended_total += sum(generate_sequence(id_range, True))
        print(
            f'Results: {total}, {extended_total}')
    return 0


if __name__ == '__main__':
    app.run(main)
