# LeetCode 2090. K Radius Subarray Averages — Medium
# https://leetcode.com/problems/k-radius-subarray-averages/
# Submission 2204402850 — Accepted, Python3
#
# My thinking: a k-radius average only exists where a full window of
# 2k + 1 elements fits, so I first compute the sum of the first window
# and then slide it one step at a time, adding the new element and
# dropping the old one, dividing by the window size each time.
# Positions without a full window stay -1.
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        if 2 * k + 1 > n:
            return ans
        window = sum(nums[:2 * k + 1])
        ans[k] = window // (2 * k + 1)
        for i in range(k + 1, n - k):
            window += nums[i + k] - nums[i - k - 1]
            ans[i] = window // (2 * k + 1)
        return ans
