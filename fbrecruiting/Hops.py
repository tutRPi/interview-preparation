from typing import List


# Write any import statements here


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    # Write your code here

    if F == 1:
        return N - P[0]

    counter = 0
    P.sort()

    while True:
        if P[0] < P[1] - 1:
            counter += P[1] - P[0] - 1
            P[0] = P[1] - 1
        else:
            # find next free slot
            pos = F
            for i in range(2, len(P)):
                if P[i] > P[i - 1] + 1:
                    pos = i
                    break
            if pos == F:
                counter += (N - P[-1]) + (F - 1)
                return counter
            else:
                offset = (P[pos] - P[pos - 1]) - 1
                counter += offset
                for i in range(pos):
                    P[i] += offset



print(getSecondsRequired(10**10, 5, [584, 78748, 225, 8885525, 55]))