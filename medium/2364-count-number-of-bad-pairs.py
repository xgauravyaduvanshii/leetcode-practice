# LeetCode 2364. Count Number of Bad Pairs — Medium
# https://leetcode.com/problems/count-number-of-bad-pairs/
# Submission 2204746048 — Accepted, Python3
#
# My thinking: a pair (i, j) is good exactly when nums[j] - nums[i] ==
# j - i, i.e. when nums[i] - i == nums[j] - j. So I count good pairs by
# grouping indices by the key nums[i] - i: each earlier index with the
# same key forms a good pair with the current one. Bad pairs are all
# pairs minus good pairs.
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        freq = {}
        good = 0
        for i, x in enumerate(nums):
            key = x - i
            good += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1
        return n * (n - 1) // 2 - good
