# LeetCode 2640. Find the Score of All Prefixes of an Array — Medium
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/
# Submission 2205107905 — Accepted, Python3
#
# My thinking: the score of a prefix is its element sum plus
# its maximum. One left-to-right pass keeps both running
# values, so each prefix score is O(1).
class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        ans = []
        total = 0
        mx = 0
        for x in nums:
            mx = max(mx, x)
            total += x + mx
            ans.append(total)
        return ans
