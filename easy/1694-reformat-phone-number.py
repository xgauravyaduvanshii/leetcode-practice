# LeetCode 1694. Reformat Phone Number — Easy
# https://leetcode.com/problems/reformat-phone-number/
# Submission 2197593975 — Accepted, Python3
#
# My thinking: first I strip everything except the
# digits. Then I cut them into groups of 3, except
# at the end — if 4 digits are left, I split them
# into two groups of 2 (a group of 1 is not
# allowed). Then I join the groups with dashes.

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = "".join(ch for ch in number if ch.isdigit())
        groups = []
        i = 0
        while len(digits) - i > 4:
            groups.append(digits[i:i + 3])
            i += 3
        if len(digits) - i == 4:
            groups.append(digits[i:i + 2])
            groups.append(digits[i + 2:i + 4])
        else:
            groups.append(digits[i:])
        return "-".join(groups)
