# 3216. Lexicographically Smallest String After a Swap (Easy)
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/
# Submission 2199988090 — Accepted, Python3
class Solution:
    def getSmallestString(self, s: str) -> str:
        # My thinking: only one swap is allowed, and it
        # must be between neighbours of the same parity.
        # The first spot where swapping makes the string
        # smaller is the best one — later swaps can only
        # change a later letter.
        chars = list(s)
        for i in range(len(chars) - 1):
            a, b = int(chars[i]), int(chars[i + 1])
            if a % 2 == b % 2 and b < a:
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                break
        return "".join(chars)
