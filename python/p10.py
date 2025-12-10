from typing import List

import z3

from answer import Answer


def solve_instance(lights: List[bool], buttons: List[List[int]]) -> int:
    s = z3.Optimize()

    switches = [z3.Bool('button_%d' % (i,)) for i in range(len(buttons))]
    for idx, target_state in enumerate(lights):
        state = z3.BoolVal(False)
        connected_switches = [switches[i] for i in range(len(switches)) if
                              idx in buttons[i]]
        for switch in connected_switches:
            state = z3.Xor(state, switch)
        s.add(state == target_state)

    press_count = z3.Sum([z3.If(v, 1, 0) for v in switches])
    s.minimize(press_count)

    if s.check() == z3.sat:
        m = s.model()
        return sum([1 for b in switches if z3.is_true(m[b])])
    return -1000


def solve(lines: List[str]) -> Answer:
    p0 = 0

    for l in lines:
        lights = []
        buttons = []
        for e in [x.strip() for x in  l.split()]:
            if e.startswith('['):
                lights = [c == '#' for c in e[1:-1]]
            if e.startswith('('):
                buttons.append([int(x) for x in e[1:-1].split(',')])
        p0 += solve_instance(lights, buttons)


    return Answer(p0, 0)
