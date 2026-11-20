class Solution:
    def minFlips(self, s: str) -> int:
        # My thinking: rotating is free, so try every rotation
        # of the doubled string against both alternating
        # patterns and keep the fewest flips any of them needs.
        n = len(s)
        t = s + s
        diff0 = [0] * (2 * n + 1)
        diff1 = [0] * (2 * n + 1)
        for i, c in enumerate(t):
            want0 = str(i % 2)
            want1 = str(1 - i % 2)
            diff0[i + 1] = diff0[i] + (c != want0)
            diff1[i + 1] = diff1[i] + (c != want1)
        best = n
        for i in range(n):
            best = min(best,
                       diff0[i + n] - diff0[i],
                       diff1[i + n] - diff1[i])
        return best
