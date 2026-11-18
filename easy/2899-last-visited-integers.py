# LeetCode 2899. Last Visited Integers — Easy
# https://leetcode.com/problems/last-visited-integers/
# Submission 2198693989 — Accepted, Python3
#
# My thinking: I keep every positive number I have
# seen, in order. Each "prev" asks for one step
# further back in that list — the first prev wants
# the last number, the next one the one before it —
# and if I run out of numbers the answer is -1. A
# new number resets the run.

from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        seen = []
        answers = []
        streak = 0
        for word in words:
            if word == "prev":
                streak += 1
                if streak <= len(seen):
                    answers.append(seen[-streak])
                else:
                    answers.append(-1)
            else:
                seen.append(int(word))
                streak = 0
        return answers
