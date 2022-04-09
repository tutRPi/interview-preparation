class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_matrix = {}
        for edge in edges:
            if edge[0] not in adj_matrix:
                adj_matrix[edge[0]] = [edge[1]]
            else:
                adj_matrix[edge[0]].append(edge[1])

            if edge[1] not in adj_matrix:
                adj_matrix[edge[1]] = [edge[0]]
            else:
                adj_matrix[edge[1]].append(edge[0])

        for u, v in edges[::-1]:
            visited = set()
            adj_matrix[u].remove(v)
            adj_matrix[v].remove(u)

            self.dfs(u, adj_matrix, visited)
            if len(visited) == len(adj_matrix.keys()):
                return [u, v]

            adj_matrix[u].append(v)
            adj_matrix[v].append(u)

    def dfs(self, start, adj_matrix, visited):
        if start not in visited:
            visited.add(start)
            for n in adj_matrix[start]:
                if n not in visited:
                    self.dfs(n, adj_matrix, visited)