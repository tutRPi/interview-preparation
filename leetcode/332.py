class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        TICKET_COUNT = len(tickets)

        connections = defaultdict(list)
        for i in range(TICKET_COUNT):
            connections[tickets[i][0]].append((tickets[i][1], i))

        for k in connections:
            connections[k].sort()

        def dfs(start, path, visited) -> List[str]:
            if len(visited) == TICKET_COUNT:
                return path

            for target, i in connections[start]:
                if i not in visited:
                    visited.add(i)
                    p = dfs(target, path + [target], visited)
                    if p: return p
                    visited.remove(i)

            return []

        return dfs("JFK", ["JFK"], set())

