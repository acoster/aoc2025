from dataclasses import dataclass
from itertools import combinations
from typing import List
from functools import reduce
import operator

import igraph as ig

from answer import Answer
from utils import Coord3D


@dataclass(frozen=True, eq=True)
class DistanceAndCoords:
    distance: float
    a: int
    b: int


def solve(lines: List[str]) -> Answer:
    coords: List[Coord3D] = []
    for line in lines:
        x, y, z = [int(e) for e in line.split(',')]
        coords.append(Coord3D(x=x, y=y, z=z))
    max_connections = len(coords)
    distances = []
    g = ig.Graph(directed=False, n=len(coords))

    for idx_a, idx_b in combinations(range(len(coords)), 2):
        a, b = coords[idx_a], coords[idx_b]
        distances.append(
            DistanceAndCoords(distance=Coord3D.distance(a, b), a=idx_a,
                              b=idx_b))

    distances.sort(key=lambda x: x.distance)
    connections = 0
    o = distances[0]
    while distances:
        o = distances.pop(0)
        if not g.are_connected(o.a, o.b):
            g.add_edge(o.a, o.b)
            connections += 1
            if connections == max_connections:
                break

    component_sizes = g.components().sizes()
    component_sizes.sort(reverse=True)
    part_one = reduce(operator.mul, component_sizes[:3], 1)

    while not g.is_connected():
        o = distances.pop(0)
        if not g.are_connected(o.a, o.b):
            g.add_edge(o.a, o.b)


    return Answer(part_one, coords[o.a].x * coords[o.b].x)
