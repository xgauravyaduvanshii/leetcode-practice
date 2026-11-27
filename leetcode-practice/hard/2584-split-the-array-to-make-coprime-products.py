# LeetCode 2584. Split the Array to Make Coprime Products — Hard
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/
# Submission 2201836176 — Accepted, Python3
#
# My thinking: a split fails exactly
# when some prime lives on both sides of
# it, so I learn where every prime
# starts and ends, then walk the split
# forward keeping the furthest any prime
# seen so far still reaches — the first
# split it never reaches past is the
# answer.

class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        n = len(nums)
        mx = max(nums)
        if mx < 2:
            # every number is 1, so every split is coprime — but a split needs
            # at least two elements
            return 0 if n >= 2 else -1
        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, mx + 1, step):
                    if spf[j] == j:
                        spf[j] = i
        last = {}
        for idx, x in enumerate(nums):
            v = x
            while v > 1:
                p = spf[v]
                last[p] = idx
                while v % p == 0:
                    v //= p
        max_last = -1
        for i in range(n - 1):
            v = nums[i]
            while v > 1:
                p = spf[v]
                if last[p] > max_last:
                    max_last = last[p]
                while v % p == 0:
                    v //= p
            if max_last <= i:
                return i
        return -1
