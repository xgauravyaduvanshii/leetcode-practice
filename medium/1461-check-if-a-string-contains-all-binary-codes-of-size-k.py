# LeetCode 1461. Check If a String Contains All Binary Codes of Size K — Medium
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Submission 2199854582 — Accepted, Python3
#
# My thinking: there are 2 to the k possible
# codes, and each one must appear as a window
# of the string. I collect every window and
# check that all of them showed up.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = {s[i:i + k] for i in range(len(s) - k + 1)}
        return len(seen) == 1 << k
