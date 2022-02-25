def tarjan(graph):
    def dfs(start_node, idx):
        stack.append(start_node)
        on_stack[start_node] = True
        idx += 1
        ids[start_node] = low[start_node] = idx
        for to in graph[start_node]:
            if ids[to] == -1:
                idx = dfs(to, idx)
            if on_stack[to]:
                low[start_node] = min(low[start_node], low[to])

        if ids[start_node] == low[start_node]:
            while True:
                n = stack.pop()
                if not n:
                    break
                on_stack[n] = False
                low[n] = ids[start_node]
                if n == start_node:
                    break
        return idx

    idx = 0
    ids = {}
    low = {}
    on_stack = {}
    stack = []
    for node in graph:
        ids[node] = -1
        low[node] = 0
        on_stack[node] = False
    for node in graph:
        if ids[node] == -1:
            idx = dfs(node, idx)

    components = {}
    for node in low:
        if low[node] not in components:
           components[low[node]] = []
        components[low[node]].append(node)
    return components.values()


if __name__ == "__main__":
    G = {
        "A": ["B", "E"],
        "B": ["F"],
        "C": ["B", "D", "G"],
        "D": ["G"],
        "E": ["A", "F"],
        "F": ["C", "G"],
        "G": ["H"],
        "H": ["D"],
    }
    components = tarjan(G)
    print(components)
