# LeetCode 2673. Make Costs of Paths Equal in a Binary Tree — Medium
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
# Submission 2205188698 — Accepted, Python3
#
# My thinking: costs can only go up, so work bottom-up. For each
# node, the best path down through it is its own cost plus the
# larger of its two children's best paths. The two children must
# be lifted to the same height, which costs the difference
# between their best paths; adding those differences over all
# internal nodes is the minimum total, because each subtree is
# fixed independently and only its height matters above it.
class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        path = [0] * (n + 1)
        ans = 0
        for i in range(n, 0, -1):
            if 2 * i > n:
                path[i] = cost[i - 1]
            else:
                left, right = path[2 * i], path[2 * i + 1]
                ans += abs(left - right)
                path[i] = cost[i - 1] + max(left, right)
        return ans
