# LeetCode 1576. Replace All ?'s to Avoid Consecutive Repeating Characters — Easy
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
# Submission 2197587410 — Accepted, Python3
#
# My thinking: for each '?', I pick the first of a,
# b, c that is different from the letter before it
# and the letter after it. Three letters are always
# enough, since at most two neighbours can block
# me.

class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        for i, ch in enumerate(chars):
            if ch == "?":
                prev = chars[i - 1] if i > 0 else ""
                nxt = chars[i + 1] if i + 1 < len(chars) and chars[i + 1] != "?" else ""
                for c in "abc":
                    if c != prev and c != nxt:
                        chars[i] = c
                        break
        return "".join(chars)
