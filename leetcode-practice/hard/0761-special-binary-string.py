# LeetCode 761. Special Binary String — Hard
# https://leetcode.com/problems/special-binary-string/
# Submission 2198673862 — Accepted, Python3
#
# My thinking: a special string splits into balanced
# blocks, and each block is a 1, a smaller special
# string, and a 0. I solve the inside of every block
# the same way and then sort the blocks biggest first
# — that ordering is what makes the whole string the
# largest possible.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        balance = 0
        start = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == "1" else -1
            if balance == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                parts.append("1" + inner + "0")
                start = i + 1
        parts.sort(reverse=True)
        return "".join(parts)
