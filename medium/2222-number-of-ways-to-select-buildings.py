# LeetCode 2222. Number of Ways to Select Buildings — Medium
# https://leetcode.com/problems/number-of-ways-to-select-buildings/
# Submission 2204507753 — Accepted, Python3
#
# My thinking: a valid triple is "010" or "101", so the middle building
# decides the pattern. I sweep once, keeping how many 0s and 1s I have
# seen on the left and how many remain on the right; each '0' in the
# middle pairs every left '1' with every right '1', and each '1' pairs
# every left '0' with every right '0'.
class Solution:
    def numberOfWays(self, s: str) -> int:
        total0 = s.count('0')
        total1 = len(s) - total0
        left0 = 0
        left1 = 0
        ans = 0
        for ch in s:
            if ch == '0':
                ans += left1 * (total1 - left1)
                left0 += 1
            else:
                ans += left0 * (total0 - left0)
                left1 += 1
        return ans
