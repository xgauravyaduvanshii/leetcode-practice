# LeetCode 1415. The k-th Lexicographical String of All Happy Strings of Length n — Medium
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# Submission 2199055120 — Accepted, Python3
#
# My thinking: a happy string never repeats a
# letter twice in a row. I build every one in
# dictionary order and pick the kth — there are
# only a few hundred at most.

from itertools import product


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ["".join(p) for p in product("abc", repeat=n) if all(a != b for a, b in zip(p, p[1:]))]
        return happy[k - 1] if k <= len(happy) else ""
