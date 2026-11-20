class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        # My thinking: the spiral can only cross in three ways — the
        # current step reaches back over the step three before it,
        # the fifth step meets the first one on the same line, or the
        # sixth step cuts across the first one from the inside.
        x = distance
        for i in range(3, len(x)):
            # 4th line crosses 1st line
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
            # 5th line meets 1st line
            if i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                return True
            # 6th line crosses 1st line
            if (i >= 5 and x[i - 2] > x[i - 4] and x[i] + x[i - 4] >= x[i - 2]
                    and x[i - 1] <= x[i - 3] and x[i - 1] + x[i - 5] >= x[i - 3]):
                return True
        return False
