# LeetCode 1723. Find Minimum Time to Finish All Jobs — Hard
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
# Submission 2201114971 — Accepted, Python3
#
# My thinking: I sort the jobs biggest first and try
# them onto the workers one by one, always pruning a
# branch the moment its busiest worker is no better
# than the best answer I already have — and I skip
# trying a job on an empty worker twice.

class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs.sort(reverse=True)
        workers = [0] * k
        best = [sum(jobs)]
        def dfs(i):
            if i == len(jobs):
                best[0] = min(best[0], max(workers))
                return
            seen = set()
            for w in range(k):
                if workers[w] in seen:
                    continue
                seen.add(workers[w])
                if workers[w] + jobs[i] >= best[0]:
                    continue
                workers[w] += jobs[i]
                dfs(i + 1)
                workers[w] -= jobs[i]
                if workers[w] == 0:
                    break
        dfs(0)
        return best[0]
