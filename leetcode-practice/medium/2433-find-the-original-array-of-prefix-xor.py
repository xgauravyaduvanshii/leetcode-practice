# LeetCode 2433. Find The Original Array of Prefix Xor — Medium
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
# Submission 2197783981 — Accepted, Python3
#
# My thinking: the first element of the original array
# is the first prefix xor. Each later element is the
# xor of the current prefix and the previous prefix,
# since xoring undoes the prefix xor.

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i] ^ pref[i - 1])
        return res
