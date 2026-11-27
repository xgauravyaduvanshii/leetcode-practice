# LeetCode 2071. Maximum Number of Tasks You Can Assign — Hard
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
# Submission 2201565735 — Accepted, Python3
#
# My thinking: I guess how many tasks I can do
# and check it — the hardest tasks first, each
# one going to the weakest worker who can manage
# it plain, or with a pill if nobody can — and
# I narrow the guess until it just fits.

import bisect


class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can(k):
            need = tasks[:k]
            have = sorted(workers[-k:])
            left = pills
            for task in reversed(need):
                i = bisect.bisect_left(have, task)
                if i < len(have):
                    have.pop(i)
                    continue
                i = bisect.bisect_left(have, task - strength)
                if i < len(have) and left > 0:
                    have.pop(i)
                    left -= 1
                    continue
                return False
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
