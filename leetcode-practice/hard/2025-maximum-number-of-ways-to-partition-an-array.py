# LeetCode 2025. Maximum Number of Ways to Partition an Array — Hard
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/
# Submission 2201552892 — Accepted, Python3
#
# My thinking: changing one number only moves
# the total and the prefix sums by the same
# gap, so for each spot I ask how many splits
# land exactly on half — with and without the
# change — and keep the best count.

from collections import Counter


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        s = 0
        for i, x in enumerate(nums):
            s += x
            prefix[i] = s
        total = s
        ans = 0
        if total % 2 == 0:
            ans = sum(1 for i in range(n - 1) if prefix[i] == total // 2)
        # right_freq holds prefix[i] for i >= j (splits only go to n-2),
        # left_freq holds prefix[i] for i < j.
        right_freq = Counter(prefix[:n - 1])
        left_freq = Counter()
        for j in range(n):
            delta = k - nums[j]
            count = 0
            t1 = total + delta
            if t1 % 2 == 0:
                count += left_freq.get(t1 // 2, 0)
            t2 = total - delta
            if t2 % 2 == 0:
                count += right_freq.get(t2 // 2, 0)
            ans = max(ans, count)
            if j < n - 1:
                right_freq[prefix[j]] -= 1
                if right_freq[prefix[j]] == 0:
                    del right_freq[prefix[j]]
                left_freq[prefix[j]] += 1
        return ans
