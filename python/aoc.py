import argparse
import doctest
import importlib
import time
from sys import exit

from si_prefix import si_format

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='')
    parser.add_argument('--problem', '-p', type=str, default='', required=True)
    ns = parser.parse_args()

    try:
        p = importlib.import_module(ns.problem, package=__package__)
    except ImportError as e:
        print(f'Failed to import {ns.problem}')
        exit(1)

    if 'solve' not in dir(p):
        print(f'{ns.problem} does not define a solve function')
        exit(1)

    doctest.testmod(p)

    if ns.input != '':
        try:
            with open(ns.input) as f:
                if 'DONT_STRIP_LINES' in dir(p):
                    lines = f.read().splitlines()
                else:
                    lines = [l.strip() for l in f.readlines()]

            start = time.perf_counter()
            result = p.solve(lines)
            runtime = time.perf_counter() - start

            print(f'{result}')
            print(f'Runtime: {si_format(runtime, 2)}s')
        except IOError as e:
            print(f'Failed to open {ns.input}: {e.strerror}')
            exit(1)
