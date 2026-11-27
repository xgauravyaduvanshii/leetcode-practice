# LeetCode 2342. Max Sum of a Pair With Equal Sum of Digits — Medium
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
# Submission 2204712785 — Accepted, Python3
#
# My thinking: two numbers can pair up only when their digit sums match,
# so I group numbers by digit sum and remember the biggest number seen
# so far in each group. For every new number I try pairing it with that
# group's best, then update the group's best — one pass, and the best
# pair sum is the answer (-1 when no group ever has two numbers).
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        best = {}
        ans = -1
        for v in nums:
            d = digit_sum(v)
            if d in best:
                ans = max(ans, best[d] + v)
                best[d] = max(best[d], v)
            else:
                best[d] = v
        return ans
