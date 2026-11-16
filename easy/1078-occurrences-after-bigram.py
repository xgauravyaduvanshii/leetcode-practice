# LeetCode 1078. Occurrences After Bigram — Easy
# https://leetcode.com/problems/occurrences-after-bigram/
# Submission 2197555650 — Accepted, Python3
#
# My thinking: I split the text into words and walk
# through them three at a time. Whenever the first
# two words match the bigram I am looking for, the
# third word goes in the answer.
#
# (Note: LeetCode spells the method findOcurrences.)

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        result = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        return result
