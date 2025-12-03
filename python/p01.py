from typing import List

from answer import Answer


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


def solve(lines: List[str]) -> Answer:
    """
    >>> solve(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'])
    Answer(part_one=3, part_two=6)
    >>> solve(['L50', 'R2', "L102"])
    Answer(part_one=2, part_two=3)
    """
    zero_stops = 0
    zero_clicks = 0
    position = 50

    for move in lines:
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

    return Answer(zero_stops, zero_clicks)
