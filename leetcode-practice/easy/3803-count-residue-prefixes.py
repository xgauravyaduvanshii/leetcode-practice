# 3803. Count Residue Prefixes (Easy)
# https://leetcode.com/problems/count-residue-prefixes/
# Submission 2200067631 — Accepted, Python3
class Solution:
    def residuePrefixes(self, s: str) -> int:
        # My thinking: walk the string one letter at a
        # time, keeping track of how many different
        # letters have shown up. A prefix counts when
        # that number matches the prefix length modulo
        # three.
        seen = set()
        count = 0
        for i, ch in enumerate(s, 1):
            seen.add(ch)
            if len(seen) == i % 3:
                count += 1
        return count
