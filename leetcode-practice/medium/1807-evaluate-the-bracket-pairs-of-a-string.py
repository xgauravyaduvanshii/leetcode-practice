# LeetCode 1807. Evaluate the Bracket Pairs of a String — Medium
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# Submission 2199940073 — Accepted, Python3
#
# My thinking: I read the string once,
# copying plain letters as they are. When I
# hit a bracket I look the key up in the
# table, writing a question mark when it is
# missing.

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        lookup = dict(knowledge)
        result = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = s.index(")", i)
                result.append(lookup.get(s[i + 1:j], "?"))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
