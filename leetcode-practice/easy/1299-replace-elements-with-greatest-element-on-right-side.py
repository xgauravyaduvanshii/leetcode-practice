# LeetCode 1299. Replace Elements with Greatest Element on Right Side — Easy
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Submission 2197568352 — Accepted, Python3
#
# My thinking: I walk from right to left, keeping
# track of the biggest number I have seen so far.
# Each position gets replaced by that biggest
# number, and then I update it with the number I
# just replaced. The last element gets -1, since
# nothing is to its right.

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)
        return arr
