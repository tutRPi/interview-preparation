def find_connected_nodes(graph, start) -> set:
    queue = [start]
    visited = set({})
    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                queue.append(n)
    return visited


if __name__ == "__main__":
    # directed graph
    G = {
        'BGI': ['LGA'],
        'CDG': ['SIN', 'BUD'],
        'DEL': ['DOH', 'CDG'],
        'DOH': [],
        'DSM': ['ORD'],
        'EWR': ['HND'],
        'EYW': ['LHR'],
        'HND': ['ICN', 'JFK'],
        'ICN': ['JFK'],
        'JFK': ['LGA'],
        'LGA': [],
        'LHR': ['SFO'],
        'ORD': ['BGI'],
        'SAN': ['EYW'],
        'SFO': ['SAN', 'DSM'],
        'SIN': [],
        'TLV': ['DEL'],
        'BUD': [],
    }
    start = "LGA"
    visited = [start]
    new_connections = []
    connections = [find_connected_nodes(G, s) for s in G.keys()]
    while len(visited) != len(G):
        for x in connections:
            for v in visited:
                if v in x:
                    x.remove(v)
        sizes = [len(x) for x in connections]
        new_airport_index = sizes.index(max(sizes))
        new_airport_name = list(G.keys())[new_airport_index]
        new_connections.append((start, new_airport_name))
        visited.extend(connections[new_airport_index])

    print(new_connections)
