# 3330. Find the Original Typed String I (Easy)
# https://leetcode.com/problems/find-the-original-typed-string-i/
# Submission 2200003667 — Accepted, Python3
class Solution:
    def possibleStringCount(self, word: str) -> int:
        # My thinking: Alice may have pressed one key
        # too long, at most once. Each run of the same
        # letter offers as many extra presses as its
        # length minus one, plus the word itself with no
        # extra press at all.
        total = 1
        run = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                run += 1
            else:
                total += run - 1
                run = 1
        return total + run - 1
