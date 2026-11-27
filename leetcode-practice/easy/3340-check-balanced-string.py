# 3340. Check Balanced String (Easy)
# https://leetcode.com/problems/check-balanced-string/
# Submission 2200003942 — Accepted, Python3
class Solution:
    def isBalanced(self, num: str) -> bool:
        # My thinking: add up the digits in even spots
        # and the digits in odd spots. The string is
        # balanced when the two sums match.
        even = sum(int(num[i]) for i in range(0, len(num), 2))
        odd = sum(int(num[i]) for i in range(1, len(num), 2))
        return even == odd
