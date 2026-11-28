# LeetCode 2592. Maximize Greatness of an Array — Medium
# https://leetcode.com/problems/maximize-greatness-of-an-array/
# Submission 2205089961 — Accepted, Python3
#
# My thinking: sort, then greedily match each element with the
# smallest larger element that is still free. A larger element
# that can serve the current smallest should, so the count of
# successful matches is the answer.
class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        ans = 0
        for x in nums:
            if x > nums[i]:
                ans += 1
                i += 1
        return ans
