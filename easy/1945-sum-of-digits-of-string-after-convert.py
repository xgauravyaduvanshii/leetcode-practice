# LeetCode 1945. Sum of Digits of String After Convert — Easy
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# Submission 2197605038 — Accepted, Python3
#
# My thinking: first I turn each letter into its
# alphabet number (a = 1, b = 2, ...) and glue them
# into one big digit string. Then I repeat k times:
# replace the string by the sum of its digits.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = "".join(str(ord(ch) - ord('a') + 1) for ch in s)
        for _ in range(k):
            num = str(sum(int(d) for d in num))
        return int(num)
