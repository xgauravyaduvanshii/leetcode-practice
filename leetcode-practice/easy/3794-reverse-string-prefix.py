# 3794. Reverse String Prefix (Easy)
# https://leetcode.com/problems/reverse-string-prefix/
# Submission 2200066003 — Accepted, Python3
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # My thinking: turn the first k letters
        # backwards and leave the rest of the string
        # exactly as it is.
        return s[:k][::-1] + s[k:]
