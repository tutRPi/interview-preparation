def shortest_path(graph, start, end) -> list:
    def solve(s):
        queue = [s]
        visited = set([])
        previous = {s: None}
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in previous:
                        previous[neighbor] = node
                        queue.append(neighbor)
        return previous

    def reconstruct_path(prev: dict) -> list:
        path = [end]
        node = end
        while node != start:
            node = prev[node]
            path.insert(0, node)
        return path

    pre = solve(start)
    return reconstruct_path(pre)


if __name__ == "__main__":
    # undirected graph
    G = {
        0: [1, 5],
        1: [2, 5],
        2: [6, 4],
        3: [],
        4: [1, 6],
        5: [4, 3],
        6: [],
    }
    assert shortest_path(G, 0, 6) == [0, 1, 2, 6]
    assert shortest_path(G, 1, 4) == [1, 2, 4]
