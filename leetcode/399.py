class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        conversion = {}
        for i, val in enumerate(values):
            (a, b) = equations[i]
            if a not in conversion:
                conversion[a] = {}
            if b not in conversion:
                conversion[b] = {}

            conversion[a][b] = val
            conversion[b][a] = 1.0 / val

        res = [-1.0] * len(queries)
        for i, (c, d) in enumerate(queries):
            if c not in conversion or d not in conversion:
                continue

            visited = set()
            queue = [(1, c)]
            while queue:
                val, node = queue.pop(0)
                if node in visited:
                    continue
                visited.add(node)

                if node == d:
                    res[i] = val
                    break

                for neighbor in conversion[node]:
                    if neighbor not in visited:
                        queue.append((val * conversion[node][neighbor], neighbor))

        return res