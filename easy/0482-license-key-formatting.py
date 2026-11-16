# LeetCode 482. License Key Formatting — Easy
# https://leetcode.com/problems/license-key-formatting/
# Submission 2197482626 — Accepted, Python3
#
# My thinking: first I strip out the dashes and make
# everything uppercase. Then I cut the string into
# groups of k from the right — the last group is
# always full, only the first one may be shorter —
# and join them back with dashes.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        parts = []
        while len(chars) > k:
            parts.append(chars[-k:])
            chars = chars[:-k]
        if chars:
            parts.append(chars)
        return "-".join(reversed(parts))
