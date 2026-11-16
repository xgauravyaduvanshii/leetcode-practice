# LeetCode 942. DI String Match — Easy
# https://leetcode.com/problems/di-string-match/
# Submission 2197545099 — Accepted, Python3
#
# My thinking: I keep the smallest and biggest
# numbers I have not used yet. An 'I' means the
# next number must be bigger, so I take the
# smallest available. A 'D' means it must be
# smaller, so I take the biggest available. The
# one number left over goes at the end.

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        result = []
        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result
