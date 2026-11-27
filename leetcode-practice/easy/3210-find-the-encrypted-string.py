# 3210. Find the Encrypted String (Easy)
# https://leetcode.com/problems/find-the-encrypted-string/
# Submission 2199985450 — Accepted, Python3
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # My thinking: encrypting moves every letter k
        # spots forward, wrapping around the end — so
        # the answer is the tail of the string followed
        # by its head.
        k %= len(s)
        return s[k:] + s[:k]
