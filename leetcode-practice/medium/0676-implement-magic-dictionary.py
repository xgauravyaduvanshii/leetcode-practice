# LeetCode 676. Implement Magic Dictionary — Medium
# https://leetcode.com/problems/implement-magic-dictionary/
# Submission 2198908408 — Accepted, Python3
#
# My thinking: a word matches when it is the same
# length as the search word and differs in exactly
# one letter. I check every dictionary word that
# way.

class MagicDictionary:
    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diffs = sum(1 for a, b in zip(word, searchWord) if a != b)
            if diffs == 1:
                return True
        return False
