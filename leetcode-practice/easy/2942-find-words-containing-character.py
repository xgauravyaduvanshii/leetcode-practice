# LeetCode 2942. Find Words Containing Character — Easy
# https://leetcode.com/problems/find-words-containing-character/
# Submission 2198703118 — Accepted, Python3
#
# My thinking: I just walk the words with their
# positions and keep the ones that contain the
# character.

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
