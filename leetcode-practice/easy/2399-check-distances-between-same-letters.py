# LeetCode 2399. Check Distances Between Same Letters — Easy
# https://leetcode.com/problems/check-distances-between-same-letters/
# Submission 2197779200 — Accepted, Python3
#
# My thinking: I note the first position of each
# letter. When I see the letter again, the distance
# between the two occurrences must match the given
# distance for that letter.

class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first = {}
        for i, ch in enumerate(s):
            if ch in first:
                if i - first[ch] - 1 != distance[ord(ch) - ord('a')]:
                    return False
            else:
                first[ch] = i
        return True
