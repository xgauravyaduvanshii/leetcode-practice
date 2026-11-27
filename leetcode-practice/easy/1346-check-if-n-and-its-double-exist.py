# LeetCode 1346. Check If N and Its Double Exist — Easy
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Submission 2197571886 — Accepted, Python3
#
# My thinking: I go through the numbers keeping the
# ones I have seen. For each new number, I check
# whether I have already seen its double, or —
# if it is even — its half. If either is there, I
# have found my pair.

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
