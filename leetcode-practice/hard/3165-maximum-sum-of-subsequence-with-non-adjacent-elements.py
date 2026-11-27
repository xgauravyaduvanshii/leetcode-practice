# LeetCode 3165. Maximum Sum of Subsequence With Non-adjacent Elements — Hard
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
# Submission 2202053666 — Accepted, Python3
#
# My thinking: each segment keeps a 2x2
# table: the best non-adjacent sum for
# the four combinations of taking or
# skipping its first and last element.
# Merging two segments tries both ways
# across the boundary — the right
# segment's first element can only be
# taken when the left's last is skipped.
# A point update rebuilds the path to
# the root, so each query reads the
# answer off the root.

from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        NEG = -10 ** 18
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        m00 = [0] * (2 * size)
        m01 = [NEG] * (2 * size)
        m10 = [NEG] * (2 * size)
        m11 = [0] * (2 * size)
        for i, v in enumerate(nums):
            p = size + i
            m00[p] = 0
            m01[p] = v
            m10[p] = 0
            m11[p] = NEG
        for i in range(size - 1, 0, -1):
            l = i * 2
            r = l + 1
            a00 = m00[l]; a01 = m01[l]; a10 = m10[l]; a11 = m11[l]
            b00 = m00[r]; b01 = m01[r]; b10 = m10[r]; b11 = m11[r]
            x = a00 + b00; y = a01 + b10
            m00[i] = x if x > y else y
            x = a00 + b01; y = a01 + b11
            m01[i] = x if x > y else y
            x = a10 + b00; y = a11 + b10
            m10[i] = x if x > y else y
            x = a10 + b01; y = a11 + b11
            m11[i] = x if x > y else y
        total = 0
        for pos, x in queries:
            p = size + pos
            m00[p] = 0
            m01[p] = x
            m10[p] = 0
            m11[p] = NEG
            p >>= 1
            while p:
                l = p * 2
                r = l + 1
                a00 = m00[l]; a01 = m01[l]; a10 = m10[l]; a11 = m11[l]
                b00 = m00[r]; b01 = m01[r]; b10 = m10[r]; b11 = m11[r]
                s = a00 + b00; t = a01 + b10
                m00[p] = s if s > t else t
                s = a00 + b01; t = a01 + b11
                m01[p] = s if s > t else t
                s = a10 + b00; t = a11 + b10
                m10[p] = s if s > t else t
                s = a10 + b01; t = a11 + b11
                m11[p] = s if s > t else t
                p >>= 1
            ans = m00[1]
            if m01[1] > ans:
                ans = m01[1]
            if ans < 0:
                ans = 0
            total += ans
        return total % MOD
