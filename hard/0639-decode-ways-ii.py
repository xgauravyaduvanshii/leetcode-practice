# LeetCode 639. Decode Ways II — Hard
# https://leetcode.com/problems/decode-ways-ii/
# Submission 2198665441 — Accepted, Python3
#
# My thinking: I count decodings one character at a
# time, keeping only the last two totals. A star alone
# is nine letters, a star before a digit is one or two
# pairs depending on the digit, and two stars together
# make fifteen pairs — every other digit just follows
# the usual one-or-two-letters rule.

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        before_last = 1  # ways for the prefix two chars back
        last = 1         # ways for the prefix one char back
        for i, ch in enumerate(s):
            ways = 0
            if ch == "*":
                ways += 9 * last
            elif ch != "0":
                ways += last
            if i > 0:
                prev_ch = s[i - 1]
                if prev_ch == "*" and ch == "*":
                    ways += 15 * before_last
                elif prev_ch == "*":
                    ways += (2 if ch <= "6" else 1) * before_last
                elif ch == "*":
                    if prev_ch == "1":
                        ways += 9 * before_last
                    elif prev_ch == "2":
                        ways += 6 * before_last
                elif prev_ch != "0" and int(prev_ch + ch) <= 26:
                    ways += before_last
            before_last, last = last, ways % MOD
        return last
