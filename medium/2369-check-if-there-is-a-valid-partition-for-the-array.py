# LeetCode 2369. Check if There is a Valid Partition For The Array — Medium
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
# Submission 2204753541 — Accepted, Python3
#
# My thinking: work backwards with dp[i] = can the suffix from i be
# partitioned. From position i I may take a pair of equal numbers, a
# triple of equal numbers, or three consecutive increasing numbers —
# each is allowed only when the rest of the suffix after it is also
# partitionable. dp[n] is true (empty suffix), and the answer is dp[0].
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            if i + 1 < n and nums[i] == nums[i + 1] and dp[i + 2]:
                dp[i] = True
            elif i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2] and dp[i + 3]:
                dp[i] = True
            elif i + 2 < n and nums[i + 1] == nums[i] + 1 and nums[i + 2] == nums[i] + 2 and dp[i + 3]:
                dp[i] = True
        return dp[0]
