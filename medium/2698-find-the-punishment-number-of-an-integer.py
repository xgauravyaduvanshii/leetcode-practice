# LeetCode 2698. Find the Punishment Number of an Integer — Medium
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
# Submission 2205194974 — Accepted, Python3
#
# My thinking: i counts when the decimal digits of i*i can be
# split into contiguous parts summing to i. A depth-first split
# tries every first-part length, pruning as soon as the running
# sum passes i (parts only grow, so a too-large part ends that
# branch); an empty remainder with a zero remainder means the
# split works. Add i*i for every i that passes.
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can(s: str, target: int) -> bool:
            if not s:
                return target == 0
            if target < 0:
                return False
            for i in range(1, len(s) + 1):
                v = int(s[:i])
                if v > target:
                    break
                if can(s[i:], target - v):
                    return True
            return False

        ans = 0
        for i in range(1, n + 1):
            if can(str(i * i), i):
                ans += i * i
        return ans
