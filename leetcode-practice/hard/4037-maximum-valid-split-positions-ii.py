# LeetCode 4037. Maximum Valid Split Positions II — Hard
# https://leetcode.com/problems/maximum-valid-split-positions-ii/
# Submission 2203527577 — Accepted, Python3
from math import gcd
from typing import List


class Solution:
    def maxValidSplits(self, nums: List[int]) -> int:
        # My thinking: for one fixed array, a split i is
        # valid exactly when the prefix gcd up to i equals
        # the suffix gcd from i + 1, so the score is the
        # count of i with pre[i] == suf[i + 1], where pre
        # and suf are the prefix and suffix gcd arrays.
        # Scoring every possible deletion in O(n) each is
        # too slow for n = 10^5. But a prefix gcd only
        # changes O(log M) times: each change at least
        # halves the value, since every new gcd divides
        # the previous one. If neither the prefix gcd nor
        # the suffix gcd changes at index i, deleting
        # nums[i] leaves every other prefix and suffix gcd
        # untouched and only merges the two neighbouring
        # split positions into one, so the score cannot
        # grow. Only the O(log M) indices where a gcd
        # actually changes (plus index 0, and the mirrored
        # end from the reversed pass) are worth deleting
        # and rescoring; the answer is the best of those
        # and of deleting nothing.
        n = len(nums)

        def calc(arr):
            m = len(arr)
            pre = [0] * m
            suf = [0] * m
            pre[0] = arr[0]
            for i in range(1, m):
                pre[i] = gcd(pre[i - 1], arr[i])
            suf[-1] = arr[-1]
            for i in range(m - 2, -1, -1):
                suf[i] = gcd(suf[i + 1], arr[i])
            ans = 0
            for i in range(m - 1):
                if pre[i] == suf[i + 1]:
                    ans += 1
            return ans

        def mark(arr):
            pos = [False] * n
            pos[0] = True
            g = arr[0]
            for i in range(1, n):
                ng = gcd(g, arr[i])
                pos[i] = ng != g
                g = ng
            return pos

        pos1 = mark(nums)
        pos2 = mark(nums[::-1])
        ans = calc(nums)
        for i in range(n):
            if pos1[i] or pos2[n - 1 - i]:
                arr = nums[:i] + nums[i + 1:]
                ans = max(ans, calc(arr))
        return ans
