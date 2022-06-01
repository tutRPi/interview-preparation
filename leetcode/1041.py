class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dir_x, dir_y = 0, 1

        for _ in range(4):
            for c in list(instructions):
                if c == "G":
                    x += dir_x
                    y += dir_y
                else:
                    if c == "L" and dir_x == 0:
                        dir_x = -dir_y
                        dir_y = 0
                    elif c == "R" and dir_y == 0:
                        dir_y = -dir_x
                        dir_x = 0
                    else:
                        dir_x, dir_y = dir_y, dir_x

            if x == y == 0:
                return True

        return False