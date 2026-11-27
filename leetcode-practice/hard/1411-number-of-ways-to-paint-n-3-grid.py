class Solution:
    def numOfWays(self, n: int) -> int:
        # My thinking: a row is either all three colours
        # different or the two ends the same — count both
        # kinds and step them forward row by row.
        MOD = 10 ** 9 + 7
        abc = 6
        aba = 6
        for _ in range(1, n):
            abc, aba = (2 * abc + 2 * aba) % MOD, (2 * abc + 3 * aba) % MOD
        return (abc + aba) % MOD
