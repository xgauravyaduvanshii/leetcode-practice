# LeetCode 2815. Max Pair Sum in an Array — Easy
# https://leetcode.com/problems/max-pair-sum-in-an-array/
# Submission 2198415850 — Accepted, Python3
#
# My thinking: two numbers can pair only when their
# biggest digit matches, so I group by that digit
# and remember the biggest number seen in each
# group. Each new number pairs with the best one
# in its group so far, and I keep the largest sum
# over all the pairs.

from typing import List


class Solution:
    def maxPairSum(self, nums: List[int]) -> int:
        best_by_digit = {}
        answer = -1
        for num in nums:
            digit = max(str(num))
            if digit in best_by_digit:
                answer = max(answer, best_by_digit[digit] + num)
                best_by_digit[digit] = max(best_by_digit[digit], num)
            else:
                best_by_digit[digit] = num
        return answer
