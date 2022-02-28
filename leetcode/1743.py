class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        hashmap = {}
        for (u, v) in adjacentPairs:
            if u not in hashmap:
                hashmap[u] = []
            hashmap[u].append(v)

            if v not in hashmap:
                hashmap[v] = []
            hashmap[v].append(u)

        # search for element with only 1 neighbor (=start/end)
        current_element = None
        for element in hashmap:
            if len(hashmap[element]) == 1:
                current_element = element
                break

        nums = []
        nums.append(current_element)
        last_element = None

        while last_element is None or len(hashmap[current_element]) != 1:
            neighbors = hashmap[current_element]
            if neighbors[0] == last_element:
                current_element, last_element = neighbors[1], current_element
            else:
                current_element, last_element = neighbors[0], current_element
            nums.append(current_element)

        return nums