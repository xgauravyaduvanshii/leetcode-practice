# 3083. Existence of a Substring in a String and Its Reverse (Easy)
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/
# Submission 2199974244 — Accepted, Python3
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # My thinking: any two-letter piece of the string
        # whose reverse also appears somewhere in the
        # string does the job. I try each neighbouring
        # pair and look for its reverse.
        for i in range(len(s) - 1):
            pair = s[i:i + 2]
            if pair[::-1] in s:
                return True
        return False
