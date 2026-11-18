# LeetCode 402. Remove K Digits — Medium
# https://leetcode.com/problems/remove-k-digits/
# Submission 2198778238 — Accepted, Python3
#
# My thinking: I build the answer left to right and
# drop any digit that is bigger than the one after
# it — that keeps the number as small as possible.
# Leftover removals come off the end, and leading
# zeros are stripped.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")
        return result if result else "0"
