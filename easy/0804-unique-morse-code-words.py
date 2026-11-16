# LeetCode 804. Unique Morse Code Words — Easy
# https://leetcode.com/problems/unique-morse-code-words/
# Submission 2197528912 — Accepted, Python3
#
# My thinking: I write out the morse code for each
# letter (a is index 0, b is 1, and so on), join
# the codes for a whole word, and put the result
# in a set. Words that sound the same collapse
# into one entry, so the size of the set is the
# number of different transformations.

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        seen = set()
        for word in words:
            code = "".join(morse[ord(ch) - ord('a')] for ch in word)
            seen.add(code)
        return len(seen)
