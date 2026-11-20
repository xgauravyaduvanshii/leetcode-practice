class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        # My thinking: each day takes a chunk of the jobs and
        # pays its hardest job — so try every place the last
        # day could start and keep the cheapest split.
        n = len(jobDifficulty)
        if n < d:
            return -1
        INF = float("inf")
        prev = [INF] * (n + 1)
        prev[0] = 0
        for day in range(1, d + 1):
            cur = [INF] * (n + 1)
            for i in range(day, n + 1):
                hardest = 0
                for j in range(i - 1, day - 2, -1):
                    hardest = max(hardest, jobDifficulty[j])
                    cur[i] = min(cur[i], prev[j] + hardest)
            prev = cur
        return prev[n]
