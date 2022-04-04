class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {key: [] for key in range(numCourses)}
        in_degree = {key: 0 for key in range(numCourses)}
        for target, start in prerequisites:
            adj_list[start].append(target)
            in_degree[target] += 1

        queue = [key for key in in_degree if in_degree[key] == 0]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            del in_degree[node]

            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []