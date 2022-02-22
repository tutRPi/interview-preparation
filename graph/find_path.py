def has_path(graph, src, dest) -> bool:
    def __has_path(graph, src, dest, visited) -> bool:
        if src == dest:
            return True
        if src in visited:
            return False

        visited.add(src)

        for neighbor in graph[src]:
            if __has_path(graph, neighbor, dest, visited):
                return True
        return False

    return __has_path(graph, src, dest, set({}))


if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['e'],
        'c': ['a', 'd'],
        'd': [],
        'e': ['c'],
    }
    assert has_path(graph, 'a', 'b') is True
    assert has_path(graph, 'b', 'a') is True
    assert has_path(graph, 'd', 'e') is False

