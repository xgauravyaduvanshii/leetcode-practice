# LeetCode 3681. Maximum XOR of Subsequences — Hard
# https://leetcode.com/problems/maximum-xor-of-subsequences/
# Submission 2203037424 — Accepted, Python3
from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        # My thinking: XOR-ing the two subsequences cancels any
        # element picked twice, so X XOR Y is just the XOR of
        # some subset of nums — and every subset is reachable
        # (put it in the first subsequence, leave the second
        # empty). So the answer is the largest XOR any subset
        # can give, which a binary linear basis finds greedily:
        # keep one basis vector per highest bit, then build the
        # answer bit by bit from the top, taking a vector
        # whenever it makes the answer bigger.
        basis = [0] * 31
        for x in nums:
            v = x
            for b in range(30, -1, -1):
                if (v >> b) & 1 == 0:
                    continue
                if basis[b] == 0:
                    basis[b] = v
                    break
                v ^= basis[b]
        ans = 0
        for b in range(30, -1, -1):
            if ans ^ basis[b] > ans:
                ans ^= basis[b]
        return ans
