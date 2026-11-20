class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        # My thinking: count sequences by their last face and
        # current run length — a face can only extend a run up
        # to its own limit.
        MOD = 10 ** 9 + 7
        dp = [[0] * 16 for _ in range(6)]
        for face in range(6):
            dp[face][1] = 1
        for _ in range(n - 1):
            new_dp = [[0] * 16 for _ in range(6)]
            for face in range(6):
                for run in range(1, rollMax[face] + 1):
                    count = dp[face][run]
                    if not count:
                        continue
                    if run < rollMax[face]:
                        new_dp[face][run + 1] = (new_dp[face][run + 1] + count) % MOD
                    for other in range(6):
                        if other != face:
                            new_dp[other][1] = (new_dp[other][1] + count) % MOD
            dp = new_dp
        return sum(sum(row) for row in dp) % MOD
