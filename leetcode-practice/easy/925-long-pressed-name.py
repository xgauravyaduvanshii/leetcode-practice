# 925. Long Pressed Name (Easy)
# https://leetcode.com/problems/long-pressed-name/
# Submission 2199965041 — Accepted, Python3
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # My thinking: walk through both strings together.
        # Every letter of the name must appear in order,
        # and the typed string may only repeat the letter
        # just typed — any other extra letter breaks it.
        i = 0
        for j, ch in enumerate(typed):
            if i < len(name) and name[i] == ch:
                i += 1
            elif j > 0 and typed[j - 1] == ch:
                continue
            else:
                return False
        return i == len(name)
