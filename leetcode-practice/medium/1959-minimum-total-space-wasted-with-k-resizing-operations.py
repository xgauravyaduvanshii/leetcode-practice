# LeetCode 1959. Minimum Total Space Wasted With K Resizing Operations — Medium
# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/
# Submission 2204259239 — Accepted, Python3
#
# My thinking: k resizing operations cut the array into k + 1
# segments, and each segment is resized once to its own maximum,
# so a segment's waste is its maximum times its length minus the
# sum of its numbers. The best total is a dynamic program: dp[i][j]
# is the least waste for the first i numbers cut into j segments,
# and I try every possible start for the last segment, adding its
# waste to the best cost of everything before it. A prefix sum
# makes each segment's waste a constant-time lookup.
class Solution:
    def minSpaceWastedKResizing(self, nums, k):
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def waste(lo, hi):
            return max(nums[lo:hi + 1]) * (hi - lo + 1) - (prefix[hi + 1] - prefix[lo])

        INF = float("inf")
        segments = min(k + 1, n)
        dp = [[INF] * (segments + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, segments) + 1):
                for p in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + waste(p, i - 1))
        return min(dp[n][1:segments + 1])
