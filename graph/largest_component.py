def largest_component(graph) -> int:
    def __explore(src, visited_nodes) -> (int, set):
        if src in visited_nodes:
            return 0, visited_nodes

        count = 1
        visited_nodes.add(src)
        for key in graph[src]:
            c, visited_nodes = __explore(key, visited_nodes)
            count += c
        return count, visited_nodes

    largest_island = 0
    visited = set({})
    for k, v in graph.items():
        val, visited = __explore(k, visited)
        if val > largest_island:
            largest_island = val

    return largest_island


if __name__ == "__main__":
    # undirected graph
    G = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    assert largest_component(G) == 4
