def shortest_path_length(graph, src, dest) -> int:
    if src == dest:
        return 0
    queue = [(src, 0)]
    visited = set({})
    path_length = -1

    while len(queue) > 0:
        node, distance = queue.pop(0)
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                if n == dest and (path_length == -1 or distance + 1 < path_length):
                    path_length = distance + 1
                queue.append((n, distance + 1))

    return path_length


if __name__ == "__main__":
    # undirected graph
    G = {
        'w': ['x', 'v'],
        'x': ['w', 'y'],
        'y': ['x', 'z'],
        'z': ['y', 'v'],
        'v': ['z', 'w'],
    }
    assert shortest_path_length(G, 'w', 'z') == 2
    assert shortest_path_length(G, 'x', 'v') == 2
