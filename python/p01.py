from absl import flags, app
from typing import List, Tuple

FLAGS = flags.FLAGS

flags.DEFINE_bool('run_tests', False, 'If true, run doctests')
flags.DEFINE_string('input', '', 'Path to input file.')


def parse_movement(movement: str) -> int:
    """
    >>> parse_movement('L10')
    -10
    >>> parse_movement('R120')
    120
    """
    if len(movement) < 2:
        return 0

    if movement[0] == 'L':
        return -int(movement[1:])

    return int(movement[1:])


def count_zeroes(movements: List[str]) -> Tuple[int, int]:
    """
    >>> count_zeroes(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'])
    (3, 6)
    """
    zero_stops = 0
    zero_clicks = 0
    position = 50

    for move in movements:
        delta = parse_movement(move)

        if abs(delta) >= 100:
            zero_clicks += abs(delta) // 100

        if delta < 0:
            delta = delta % -100
        else:
            delta = delta % 100

        if position != 0:
            if delta < 0 and int(position) + delta <= 0:
                zero_clicks += 1
            elif delta > 0 and int(position) + delta >= 100:
                zero_clicks += 1

        position = (position + delta) % 100

        if position == 0:
            zero_stops += 1

    return zero_stops, zero_clicks


def main(argv):
    if FLAGS.run_tests:
        import doctest
        doctest.testmod()
        return

    if FLAGS.input != '':
        with open(FLAGS.input) as f:
            movements = [l.strip() for l in f.readlines()]

        response_one, response_two = count_zeroes(movements)
        print(f'Response: {response_one}, {response_two}')


if __name__ == '__main__':
    app.run(main)
