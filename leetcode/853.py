class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        velocity = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        counts = len(position)
        velocity.sort(reverse=True)

        velo = velocity[0][1]
        for i in range(1, len(velocity)):
            if velocity[i][1] <= velo:
                counts -= 1
            else:
                velo = velocity[i][1]

        return counts