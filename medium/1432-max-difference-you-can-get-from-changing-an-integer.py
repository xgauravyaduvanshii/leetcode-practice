# LeetCode 1432. Max Difference You Can Get From Changing an Integer — Medium
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# Submission 2199056885 — Accepted, Python3
#
# My thinking: to go big I turn the first
# non-nine digit into nine. To go small I turn
# the first digit into one, or if it already is
# one, the first later digit that is not zero
# or one into zero.

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        high = s
        for ch in s:
            if ch != "9":
                high = s.replace(ch, "9")
                break
        low = s
        if s[0] != "1":
            low = s.replace(s[0], "1")
        else:
            for ch in s[1:]:
                if ch not in "01":
                    low = s.replace(ch, "0")
                    break
        return int(high) - int(low)
