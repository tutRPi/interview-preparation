class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {k: 0 for k in range(numCourses)}
        connections = {k: [] for k in range(numCourses)}
        for s, t in prerequisites:
            in_degree[t] += 1
            connections[s].append(t)

        queue = [k for k in range(numCourses) if in_degree[k] == 0]
        while queue:
            node = queue.pop(0)
            for nei in connections[node]:
                if in_degree[nei] == 0:
                    return False

                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return max(in_degree.values()) == 0