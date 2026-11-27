# LeetCode 2002. Maximum Product of the Length of Two Palindromic Subsequences — Medium
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
# Submission 2204124035 — Accepted, Python3
#
# My thinking:
# The string is at most 12 characters long, so there are only 2^12 = 4096
# possible subsequences, and I can look at every one of them by its
# bitmask: bit i set means character s[i] is part of the subsequence.
# For each mask I build its subsequence and check whether it reads the
# same forwards and backwards; if it does, I record the mask's length.
# Two subsequences are allowed together only when they use no character
# in common, which for bitmasks is simply mask1 & mask2 == 0.
# So I try every pair of palindromic masks that do not overlap and keep
# the biggest product of their lengths. With at most 4096 masks this
# pair check is cheap, and it is guaranteed to find the best answer
# because every possible pair of disjoint palindromic subsequences is
# examined exactly once.

from typing import List


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pal_len = {}
        for mask in range(1, 1 << n):
            sub = "".join(s[i] for i in range(n) if mask >> i & 1)
            if sub == sub[::-1]:
                pal_len[mask] = len(sub)

        best = 0
        masks = list(pal_len)
        for i in range(len(masks)):
            for j in range(i, len(masks)):
                m1, m2 = masks[i], masks[j]
                if m1 & m2 == 0:
                    best = max(best, pal_len[m1] * pal_len[m2])
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct("leetcodecom") == 9, sol.maxProduct("leetcodecom")
    assert sol.maxProduct("bb") == 1
    assert sol.maxProduct("accdbba") == 8
    print("All samples pass.")
