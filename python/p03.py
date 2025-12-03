from typing import List

from absl import flags, app

FLAGS = flags.FLAGS
flags.DEFINE_string('input', '', 'Path to input file.')


def find_joltage(bank: str, num_digits: int) -> int:
    """
    >>> find_joltage('987654321111111', 2)
    98
    >>> find_joltage('811111111111119', 2)
    89
    >>> find_joltage('234234234234278', 2)
    78
    >>> find_joltage('987654321111111', 12)
    987654321111
    """
    result = 0
    bank_length = len(bank)
    idx_start = 0

    for i in range(num_digits):
        # Don't search the last num_digits - i characters.
        idx_end = bank_length - (num_digits - i - 1)

        # Find the index of the largest character in the search window.
        idx_max = max(range(idx_start, idx_end), key=bank.__getitem__)

        result = result * 10 + int(bank[idx_max])

        idx_start = idx_max + 1

    return result


def main(argv: List[str]) -> int:
    import doctest
    doctest.testmod()

    if FLAGS.input != '':
        with open(FLAGS.input) as f:
            total_one = 0
            total_two = 0

            for line in f.readlines():
                line = line.strip()
                total_one += find_joltage(line, 2)
                total_two += find_joltage(line, 12)

            print(f'{total_one}, {total_two}')

if __name__ == '__main__':
    app.run(main)
