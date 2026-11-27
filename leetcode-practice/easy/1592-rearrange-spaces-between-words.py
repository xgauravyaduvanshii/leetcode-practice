# LeetCode 1592. Rearrange Spaces Between Words — Easy
# https://leetcode.com/problems/rearrange-spaces-between-words/
# Submission 2197588392 — Accepted, Python3
#
# My thinking: I count all the spaces and split the
# text into words. The spaces are shared equally
# between the gaps, and any leftover goes at the
# end. With a single word, all the spaces just
# trail behind it.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(" ")
        if len(words) == 1:
            return words[0] + " " * spaces
        between, extra = divmod(spaces, len(words) - 1)
        return (" " * between).join(words) + " " * extra
