from typing import List


# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    S.sort()
    additional = (S[0] - 1) // (K + 1)
    for i in range(len(S)):
        if i < len(S) - 1:
            free_seats = S[i + 1] - S[i] - 1
            additional += (free_seats - K) // (K + 1)

    additional += (N - S[-1]) // (K + 1)

    return additional
