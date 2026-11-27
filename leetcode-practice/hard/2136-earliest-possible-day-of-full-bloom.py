# LeetCode 2136. Earliest Possible Day of Full Bloom — Hard
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
# Submission 2201585159 — Accepted, Python3
#
# My thinking: while one seed is in the ground
# the others are still being planted, so the
# seed that takes longest to grow should go in
# first — plant in order of longest grow time
# and the last bloom is the answer.

class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        order = sorted(range(len(plantTime)), key=lambda i: -growTime[i])
        day = 0
        ans = 0
        for i in order:
            day += plantTime[i]
            ans = max(ans, day + growTime[i])
        return ans
