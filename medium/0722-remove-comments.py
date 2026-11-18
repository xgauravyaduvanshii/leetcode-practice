# LeetCode 722. Remove Comments — Medium
# https://leetcode.com/problems/remove-comments/
# Submission 2198922244 — Accepted, Python3
#
# My thinking: I read the source character by
# character, tracking whether I am inside a block
# comment. Line comments end the line, block
# comments end at their closing pair, and
# everything else is copied through.

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        current = []
        for line in source:
            i = 0
            while i < len(line):
                if not in_block and line[i:i + 2] == "//":
                    break
                if not in_block and line[i:i + 2] == "/*":
                    in_block = True
                    i += 2
                elif in_block and line[i:i + 2] == "*/":
                    in_block = False
                    i += 2
                elif not in_block:
                    current.append(line[i])
                    i += 1
                else:
                    i += 1
            if not in_block and current:
                result.append("".join(current))
                current = []
        return result
