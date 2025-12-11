from answer import Answer
from typing import List

import igraph as ig

def solve(lines: List[str]) -> Answer:
    graph = ig.Graph(directed=True)
    name_to_id = {}
    id_to_connections = {}

    for idx, l in enumerate(lines):
        src, connections = l.split(': ')
        name_to_id[src] = idx
        id_to_connections[idx] = connections.split()
    name_to_id['out'] = len(name_to_id)

    graph.add_vertices(len(name_to_id))
    for src, targets in id_to_connections.items():
        for target in targets:
            graph.add_edge(src, name_to_id[target])

    all_paths = graph.get_all_simple_paths(v=name_to_id['you'], to=name_to_id['out'])

    return Answer(len(all_paths), 0)