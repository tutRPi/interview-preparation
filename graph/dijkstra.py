def find_lowest(distance_array) -> int:
    index = 0
    for i, (k, v) in enumerate(distance_array):
        if distance_array[i][1] > v:
            index = i
    return index


def dijkstra(graph: dict, begin) -> (dict, dict):
    distances = dict()
    previous = dict()
    distance_array = [(begin, 0)]
    for k in graph.keys():
        distances[k] = None
        previous[k] = None
    distances[begin] = 0
    visited = []

    while len(distance_array) > 0:
        # find lowest distance
        index = find_lowest(distance_array)
        (node, dist) = distance_array.pop(index)
        if node not in visited:
            visited.append(node)
            for (neighbor, weight) in G[node]:
                distance_array.append((neighbor, dist + weight))
                if distances[neighbor] is None or dist + weight < distances[neighbor]:
                    distances[neighbor] = dist + weight
                    previous[neighbor] = node
    return distances, previous


if __name__ == "__main__":
    G = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 3),('D', 2)],
        'C': [('D', 4),('E', 5)],
        'D': [],
        'E': [('D', 1)],
    }
    dist, prev = dijkstra(G, "A")
    assert dist['A'] == 0
    assert dist['B'] == 4
    assert dist['C'] == 2
    assert dist['D'] == 6
    assert dist['E'] == 7

    assert prev['A'] is None
    assert prev['B'] == 'A'
    assert prev['C'] == 'A'
    assert prev['D'] == 'B'
    assert prev['E'] == 'C'
