from typing import List

from answer import Answer

def solve(lines: List[str]) -> Answer:
    i = 0
    shape_areas = []

    while i < len(lines):
        if 'x' in lines[i]:
            break

        area = 0
        for j in range(1, 4):
            area += len([x for x in lines[i + j] if x == '#'])
        shape_areas.append(area)
        i+= 5

    fitting = 0

    for line in lines[i:]:
        area, presents = line.split(': ')
        a, b = [int(x) for x in area.split('x')]

        total_area = a * b
        required_area = 0
        for idx, quantity in enumerate((int(x) for x in presents.split())):
            required_area += shape_areas[idx] * quantity

        if required_area <= total_area:
            fitting += 1

    return Answer(fitting, None)