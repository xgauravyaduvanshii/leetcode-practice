# LeetCode 1089. Duplicate Zeros — Easy
# https://leetcode.com/problems/duplicate-zeros/
# Submission 2197556005 — Accepted, Python3
#
# My thinking: I work backwards so I never overwrite
# a number I still need. First I count the zeros
# — each one pushes everything after it one place
# to the right. Walking from the end, I copy each
# number to its shifted spot, and when I meet a
# zero I write it twice (if both copies fit).

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
