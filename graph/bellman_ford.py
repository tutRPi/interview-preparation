import math


def bellman_ford(graph, starting_node) -> dict:
    distances = dict()
    edges = [(s, t, w) for s in graph.keys() for (t, w) in graph[s]]
    for k in graph.keys():
        distances[k] = math.inf
    distances[starting_node] = 0

    for i in enumerate(graph):
        for s, t, w in edges:
            if distances[s] + w < distances[t]:
                distances[t] = distances[s] + w

    for i in enumerate(graph):
        for s, t, w in edges:
            if distances[s] + w < distances[t]:
                distances[t] = -math.inf

    return distances


if __name__ == "__main__":
    G = {
        0: [(1, 5)],
        1: [(2, 20), (5, 30), (6, 60)],
        2: [(3, 10), (4, 75)],
        3: [(2, -15)],
        4: [(9, 100)],
        5: [(4, 25), (6, 5), (8, 50)],
        6: [(7, -50)],
        7: [(8, -10)],
        8: [],
        9: [],
    }
    dist = bellman_ford(G, 0)
    print(dist)

