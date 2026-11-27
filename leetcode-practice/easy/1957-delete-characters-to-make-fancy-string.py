# LeetCode 1957. Delete Characters to Make Fancy String — Easy
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Submission 2197605531 — Accepted, Python3
#
# My thinking: I build the answer one letter at a
# time. A letter is kept unless it would make
# three identical letters in a row — that is, the
# last two letters already in the answer are both
# the same as it.

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for ch in s:
            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                continue
            res.append(ch)
        return "".join(res)
