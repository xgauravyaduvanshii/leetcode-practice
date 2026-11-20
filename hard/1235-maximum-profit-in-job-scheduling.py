import bisect


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # My thinking: sort the jobs by end time, then each job
        # either skips or takes its profit plus the best profit
        # of everything ending before it starts.
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [job[0] for job in jobs]
        dp = [0] * (len(jobs) + 1)
        for i, (end, start, money) in enumerate(jobs, 1):
            j = bisect.bisect_right(ends, start)
            dp[i] = max(dp[i - 1], money + dp[j])
        return dp[-1]
