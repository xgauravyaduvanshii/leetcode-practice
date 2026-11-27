# LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero — Medium
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
# Submission 2204622815 — Accepted, Python3
#
# My thinking: the AND of a group is greater than zero exactly when some
# bit is set in every number of the group. So for each of the 24 bits I
# count how many candidates have that bit set; the largest such count is
# the answer, because all those numbers together have that bit in their AND.
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        ans = 0
        for b in range(24):
            cnt = 0
            for x in candidates:
                if (x >> b) & 1:
                    cnt += 1
            ans = max(ans, cnt)
        return ans
