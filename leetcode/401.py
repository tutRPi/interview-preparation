class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []

        solutions = set()  # (0b0000, 0b000000)
        self._search((0b0000, 0b000000), solutions, turnedOn, 0)
        return [str(s[0]) + ":" + ("00" + str(s[1]))[-2:] for s in solutions]

    def _is_valid(self, state, turnedOn):
        return state[0] < 12 and state[1] < 60 and \
               state[0].bit_count() + state[1].bit_count() == turnedOn

    def _generate_candidates(self, state, at_position):
        h, m = state
        if at_position >= 4:
            at_position -= 4
            return [
                (h, m | (1 << (5 - at_position))),
                (h, m & (2 ** 6 - 1 - 2 ** (5 - at_position)))
            ]
        else:
            return [
                (h | (1 << (3 - at_position)), m),
                (h & (2 ** 4 - 1 - 2 ** (3 - at_position)), m)
            ]

    def _search(self, state, solutions, turnedOn, from_position):
        if self._is_valid(state, turnedOn):
            solutions.add(state)

        for i in range(from_position, 10):
            for c in self._generate_candidates(state, i):
                self._search(c, solutions, turnedOn, i + 1)