from typing import List

from absl import flags, app

FLAGS = flags.FLAGS
flags.DEFINE_string('input', '', 'Path to input file.')


def find_joltage(bank: str) -> int:
    """
    >>> find_joltage('987654321111111')
    98
    >>> find_joltage('811111111111119')
    89
    >>> find_joltage('234234234234278')
    78
    """
    current_max = 0

    for i in range(0, len(bank) - 1):
        v = int(bank[i]) * 10 + int(max(bank[i + 1:]))
        if v > current_max:
            current_max = v

    return current_max


def main(argv: List[str]) -> int:
    import doctest
    doctest.testmod()

    if FLAGS.input != '':
        with open(FLAGS.input) as f:
            total = 0
            for line in f.readlines():
                total += find_joltage(line.strip())

            print(f'Total: {total}')

if __name__ == '__main__':
    app.run(main)
