# LeetCode 2190. Most Frequent Number Following Key In an Array — Easy
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
# Submission 2197616959 — Accepted, Python3
#
# My thinking: every time the key appears, I note
# which number comes right after it. The number
# that follows the key most often is the answer.

from collections import Counter


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counts = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1
        return counts.most_common(1)[0][0]
