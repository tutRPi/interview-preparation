def dfs(i, graph, node, visited, ordering) -> int:
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            i = dfs(i, graph, neighbor, visited, ordering)
    ordering[i] = node
    return i - 1


def topological_sort(graph) -> list:
    ordering = [None] * len(graph)
    visited = []
    i = len(graph) - 1
    for node in graph.keys():
        if node not in visited:
            i = dfs(i, graph, node, visited, ordering, )

    return ordering


if __name__ == "__main__":
    # directed graph
    G = {
        'A': ['D'],
        'B': ['D'],
        'C': ['A', 'B'],
        'D': ['G', 'H'],
        'E': ['A', 'D', 'F'],
        'F': ['J', 'K'],
        'G': ['I'],
        'H': ['I', 'J'],
        'I': ['L'],
        'J': ['L', 'M'],
        'K': ['J'],
        'L': [],
        'M': [],
    }
    result = topological_sort(G)
    print(result)
    assert result.index('C') < result.index('A')
    assert result.index('E') < result.index('A')
    assert result.index('J') < result.index('M')
    assert result.index('J') < result.index('L')
