# LeetCode 1832. Check if the Sentence Is Pangram — Easy
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Submission 2197600390 — Accepted, Python3
#
# My thinking: a pangram uses all 26 letters, so
# the set of distinct letters in the sentence must
# have exactly 26 members.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
