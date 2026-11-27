# LeetCode 2566. Maximum Difference by Remapping a Digit — Easy
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
# Submission 2197804361 — Accepted, Python3
#
# My thinking: to make the biggest number I replace
# the first digit that is not 9 with 9; to make the
# smallest I replace the first digit that is not 0
# with 0. The answer is the difference of the two.

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mx = s
        for ch in s:
            if ch != '9':
                mx = s.replace(ch, '9')
                break
        mn = s
        for ch in s:
            if ch != '0':
                mn = s.replace(ch, '0')
                break
        return int(mx) - int(mn)
