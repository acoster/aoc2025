import operator
from collections import defaultdict
from functools import reduce
from typing import List

from answer import Answer

DONT_STRIP_LINES = True

def cephalopod_numbers(operators: List[str]) -> List[int]:
    """
    >>> cephalopod_numbers(["123", " 45", "  6"])
    [1, 24, 356]
    >>> cephalopod_numbers(["328", "64 ", "98 "])
    [369, 248, 8]
    """
    width = len(operators[0])

    result = []

    for i in range(width):
        result.append(''.join(x[i] for x in operators))

    return [int(x) for x in result]

def solve(lines: List[str]) -> Answer:
    operators = defaultdict(list)

    last_line = lines[-1]
    start_positions = [idx for idx in range(len(last_line)) if
                              last_line[idx] != ' ']
    ops = [last_line[idx] for idx in start_positions]

    widths = [start_positions[i + 1] - start_positions[i] - 1 for i in range(len(start_positions) - 1)]
    widths.append(max([len(l) - start_positions[-1] for l in lines[:-1]]))

    for line in lines[:-1]:
        for column, (start, width) in enumerate(zip(start_positions, widths)):
            op = line[start:start + width]
            op = op + (width - len(op)) * ' '
            operators[column].append(op)

    part_one, part_two = 0, 0

    for column, operation in enumerate(ops):
        first_part_operators = [int(o) for o in operators[column]]
        second_part_operators = cephalopod_numbers(operators[column])
        if operation == '+':
            part_one += sum(first_part_operators)
            part_two += sum(second_part_operators)
        elif operation == '*':
            part_one += reduce(operator.mul,first_part_operators, 1)
            part_two += reduce(operator.mul, second_part_operators, 1)

    return Answer(part_one, part_two)
