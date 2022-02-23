def connected_components(graph) -> int:
    def explore(visited_elems, src) -> set:
        if src not in visited_elems:
            visited_elems.add(src)
            for neighbor in graph[src]:
                visited_elems = explore(visited_elems, neighbor)
        return visited_elems

    count = 0
    visited = set({})
    for k, v in graph.items():
        if k in visited:
            continue
        visited = explore(visited, k)
        count += 1
    return count


if __name__ == "__main__":
    # undirected graph
    G = {
        1: [2],
        2: [1],
        3: [],
        4: [6],
        5: [6],
        6: [4, 5, 7, 8],
        7: [6],
        8: [6],
    }
    assert connected_components(G) == 3
