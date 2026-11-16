# LeetCode 844. Backspace String Compare — Easy
# https://leetcode.com/problems/backspace-string-compare/
# Submission 2197533707 — Accepted, Python3
#
# My thinking: I type out each string the way a
# backspace key would — every '#' deletes the last
# letter I typed, if there is one. Then I just
# compare the two finished strings.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(text):
            result = []
            for ch in text:
                if ch == '#':
                    if result:
                        result.pop()
                else:
                    result.append(ch)
            return "".join(result)
        return process(s) == process(t)
