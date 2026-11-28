# LeetCode 2568. Minimum Impossible OR — Medium
# https://leetcode.com/problems/minimum-impossible-or/
# Submission 2205073786 — Accepted, Python3
#
# My thinking: a power of two can only be formed by OR-ing the
# number itself — any other element carrying that bit carries
# extra bits too. So the smallest non-expressible positive
# integer is the smallest power of two missing from the array.
class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        present = set(nums)
        ans = 1
        while ans in present:
            ans <<= 1
        return ans
