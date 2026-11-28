# LeetCode 2442. Count Number of Distinct Integers After Reverse Operations — Medium
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
# Submission 2204946695 — Accepted, Python3
#
# My thinking: every number and its digit-reversal both end up in
# the array, so put them all in a set and count it. Reversing a
# number is just repeated take-the-last-digit.
class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        seen = set(nums)
        for x in nums:
            rev = 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            seen.add(rev)
        return len(seen)
