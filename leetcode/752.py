class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = [('0000', 0)]

        while queue:
            current, turns = queue.pop(0)

            if current in visited or current in deadends:
                continue

            if current == target:
                return turns

            visited.add(current)
            for i in range(4):
                num = int(current[i])
                neighbors = [num - 1, num + 1]
                if num == 0:
                    neighbors[0] = 9
                elif num == 9:
                    neighbors[1] = 0

                for n in neighbors:
                    new_combination = current[0:i] + str(n) + current[i + 1:]
                    if new_combination not in visited and new_combination not in deadends:
                        queue.append((new_combination, turns + 1))
        return -1