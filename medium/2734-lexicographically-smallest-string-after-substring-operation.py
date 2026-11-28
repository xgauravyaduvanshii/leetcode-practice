# LeetCode 2734. Lexicographically Smallest String After Substring Operation — Medium
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/
# Submission 2205220193 — Accepted, Python3
#
# My thinking: decreasing a letter makes the string smaller,
# so start at the first non-'a' and decrease the whole
# contiguous run of non-'a' letters after it — stopping at the
# next 'a' avoids turning an 'a' into a 'z' and making the
# string larger. If the string is all 'a's, the only move is
# to turn the last letter into a 'z'.
class Solution:
    def smallestString(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        i = 0
        while i < n and chars[i] == "a":
            i += 1
        if i == n:
            chars[-1] = "z"
        else:
            while i < n and chars[i] != "a":
                chars[i] = chr(ord(chars[i]) - 1)
                i += 1
        return "".join(chars)
