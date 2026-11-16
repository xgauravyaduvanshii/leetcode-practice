# LeetCode 1678. Goal Parser Interpretation — Easy
# https://leetcode.com/problems/goal-parser-interpretation/
# Submission 2197592876 — Accepted, Python3
#
# My thinking: the command is just three pieces —
# "G" stays "G", "()" becomes "o", and "(al)"
# becomes "al". Two simple replacements do the
# whole job.

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
