# LeetCode 2195. Append K Integers With Minimal Sum — Medium
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/
# Submission 2204496290 — Accepted, Python3
#
# My thinking: the cheapest numbers to append are the smallest positive
# integers not already in the array. I walk the sorted unique values and
# fill the gaps before each one, taking as many as I still need from
# each gap using the arithmetic-series sum; any remainder is filled with
# the integers right after the largest existing value.
class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        total = 0
        prev = 0
        remaining = k
        for x in sorted(set(nums)):
            if remaining == 0:
                break
            gap = x - prev - 1
            if gap > 0:
                take = gap if gap < remaining else remaining
                total += take * prev + take * (take + 1) // 2
                remaining -= take
            if x > prev:
                prev = x
        if remaining > 0:
            total += remaining * prev + remaining * (remaining + 1) // 2
        return total
