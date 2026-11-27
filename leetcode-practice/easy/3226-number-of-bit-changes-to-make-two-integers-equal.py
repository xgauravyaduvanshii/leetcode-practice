# 3226. Number of Bit Changes to Make Two Integers Equal (Easy)
# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/
# Submission 2199988768 — Accepted, Python3
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # My thinking: a bit can only be turned from 1
        # to 0, never the other way. So if k needs a 1
        # where n has a 0, it is impossible — otherwise
        # the answer is how many bits differ.
        if k & ~n:
            return -1
        return bin(n ^ k).count("1")
