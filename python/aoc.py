import importlib
import time

from absl import flags, app
from si_prefix import si_format

FLAGS = flags.FLAGS
flags.DEFINE_string('input', '', 'Path to input file.')
flags.DEFINE_string('problem', '', 'Problem library (e.g. p01)')


def main(argv) -> int:
    if len(FLAGS.problem) == 0:
        print('--problem is required')
        return 1

    try:
        p = importlib.import_module(FLAGS.problem, package=__package__)
    except ImportError:
        print(f'Failed to import {FLAGS.problem}')
        return 1

    assert 'solve' in dir(p)

    import doctest
    doctest.testmod(p)

    if FLAGS.input != '':
        try:
            with open(FLAGS.input) as f:
                if 'DONT_STRIP_LINES' in dir(p):
                    lines = f.read().splitlines()
                else:
                    lines = [l.strip() for l in f.readlines()]

            start = time.perf_counter()
            result = p.solve(lines)
            runtime = time.perf_counter() - start

            print(f'{result}')
            print(f'Runtime: {si_format(runtime, 2)}s')
        except IOError:
            print(f'Failed to open {FLAGS.input}')
            return 1

    return 0


if __name__ == '__main__':
    app.run(main)
