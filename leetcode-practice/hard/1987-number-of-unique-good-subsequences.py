# LeetCode 1987. Number of Unique Good Subsequences — Hard
# https://leetcode.com/problems/number-of-unique-good-subsequences/
# Submission 2201292025 — Accepted, Python3
#
# My thinking: a 1 extends every good run so far
# plus itself, while a 0 only extends the runs
# ending in 1 — and the lone 0 counts once at the
# end, since a leading zero is never allowed.

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10 ** 9 + 7
        f0 = f1 = 0
        has_zero = False
        for ch in binary:
            if ch == '1':
                f1 = (f1 + f0 + 1) % MOD
            else:
                has_zero = True
                f0 = (f0 + f1) % MOD
        return (f0 + f1 + (1 if has_zero else 0)) % MOD
