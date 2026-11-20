# 4048. Count Values With Equally Spaced Occurrences I (Easy)
# https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/
# Submission 2200099894 — Accepted, Python3
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        # My thinking: I collect where each value
        # appears. A value is special when it appears
        # exactly three times, with the middle one
        # sitting exactly halfway between the other
        # two.
        positions = {}
        for i, x in enumerate(nums):
            positions.setdefault(x, []).append(i)
        ans = 0
        for idxs in positions.values():
            if len(idxs) == 3 and idxs[1] - idxs[0] == idxs[2] - idxs[1]:
                ans += 1
        return ans
