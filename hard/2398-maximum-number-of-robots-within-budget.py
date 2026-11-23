# LeetCode 2398. Maximum Number of Robots Within Budget — Hard
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/
# Submission 2201716257 — Accepted, Python3
#
# My thinking: a longer run only costs
# more, so I stretch a window as far as
# it fits and shrink it from the left when
# it breaks the budget — the widest window
# I ever hold is the answer.

from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        n = len(chargeTimes)
        dq = deque()
        run_sum = 0
        left = 0
        ans = 0
        for right in range(n):
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            run_sum += runningCosts[right]
            while dq and chargeTimes[dq[0]] + (right - left + 1) * run_sum > budget:
                if dq[0] == left:
                    dq.popleft()
                run_sum -= runningCosts[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
