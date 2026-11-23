# LeetCode 2301. Match Substring After Replacement — Hard
# https://leetcode.com/problems/match-substring-after-replacement/
# Submission 2201665653 — Accepted, Python3
#
# My thinking: a replacement only ever
# turns one letter into another, so I try
# every starting spot and check letter by
# letter whether each one already matches
# or is allowed to become the one it faces.

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        allowed = {}
        for old, new in mappings:
            allowed.setdefault(old, set()).add(new)
        n, m = len(s), len(sub)
        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                if sub[j] == s[i + j]:
                    continue
                if s[i + j] in allowed.get(sub[j], ()): 
                    continue
                ok = False
                break
            if ok:
                return True
        return False
