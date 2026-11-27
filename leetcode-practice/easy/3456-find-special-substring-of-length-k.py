# 3456. Find Special Substring of Length K (Easy)
# https://leetcode.com/problems/find-special-substring-of-length-k/
# Submission 2200019276 — Accepted, Python3
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        # My thinking: a special substring is k copies
        # of the same letter in a row. I slide a window
        # of length k along the string and check whether
        # every letter inside it matches the first one.
        for start in range(len(s) - k + 1):
            if len(set(s[start:start + k])) == 1:
                return True
        return False
