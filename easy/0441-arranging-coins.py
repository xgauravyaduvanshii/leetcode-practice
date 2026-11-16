# LeetCode 441. Arranging Coins — Easy
# https://leetcode.com/problems/arranging-coins/
# Submission 2197476371 — Accepted, Python3
#
# My thinking: a staircase with k full rows needs
# 1 + 2 + ... + k = k * (k + 1) / 2 coins. So I
# binary search for the biggest k whose total still
# fits in n coins.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            if total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
