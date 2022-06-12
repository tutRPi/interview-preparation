class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = defaultdict(int)
        for n in hand:
            counts[n] += 1

        groups = len(hand) // groupSize
        hand.sort()
        i = 0

        while i < len(hand):
            min_val = hand[i]
            for j in range(groupSize):
                if counts[min_val] == 1:
                    del counts[min_val]
                else:
                    counts[min_val] -= 1

                if j != groupSize - 1:
                    if min_val + 1 in counts:
                        min_val += 1
                    else:
                        return False
            # next min_val
            while i < len(hand) and hand[i] not in counts:
                i += 1
        return True