# LeetCode 1640. Check Array Formation Through Concatenation — Easy
# https://leetcode.com/problems/check-array-formation-through-concatenation/
# Submission 2197591408 — Accepted, Python3
#
# My thinking: I map each piece to its first number.
# Then I walk through the target array — each
# position must start a piece, and the whole piece
# has to match the array from there. If any piece
# does not match, the answer is false.

class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        starts = {piece[0]: piece for piece in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in starts:
                return False
            piece = starts[arr[i]]
            for value in piece:
                if i >= len(arr) or arr[i] != value:
                    return False
                i += 1
        return True
