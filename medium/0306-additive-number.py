# LeetCode 306. Additive Number — Medium
# https://leetcode.com/problems/additive-number/
# Submission 2198737161 — Accepted, Python3
#
# My thinking: the first two numbers decide the
# whole sequence, so I try every split for them —
# skipping any number with a leading zero — and
# then check whether the rest of the string is
# exactly the sums that follow.

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for first_end in range(1, n):
            first = num[:first_end]
            if len(first) > 1 and first[0] == "0":
                break
            for second_end in range(first_end + 1, n):
                second = num[first_end:second_end]
                if len(second) > 1 and second[0] == "0":
                    break
                if self._follows(num, second_end, int(first), int(second)):
                    return True
        return False

    def _follows(self, num: str, start: int, first: int, second: int) -> bool:
        while start < len(num):
            expected = str(first + second)
            if not num.startswith(expected, start):
                return False
            start += len(expected)
            first, second = second, first + second
        return True
