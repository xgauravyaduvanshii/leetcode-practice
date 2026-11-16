# LeetCode 500. Keyboard Row — Easy
# https://leetcode.com/problems/keyboard-row/
# Submission 2197485651 — Accepted, Python3
#
# My thinking: I put each keyboard row in a set.
# A word works if all of its letters (in lowercase)
# fit inside a single row's set — that is just a
# subset check.

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []
        for word in words:
            letters = set(word.lower())
            if any(letters <= row for row in rows):
                result.append(word)
        return result
