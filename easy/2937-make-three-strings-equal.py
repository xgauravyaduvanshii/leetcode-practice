# LeetCode 2937. Make Three Strings Equal — Easy
# https://leetcode.com/problems/make-three-strings-equal/
# Submission 2198702430 — Accepted, Python3
#
# My thinking: the only letters I can keep are the
# ones all three strings share from the start — the
# common prefix. Everything past it has to be deleted
# from all three strings. If there is no common
# prefix at all, the strings can never be made equal,
# because a string may not be emptied completely.

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        common = 0
        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                common += 1
            else:
                break
        if common == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * common
