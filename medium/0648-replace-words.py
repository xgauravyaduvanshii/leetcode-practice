# LeetCode 648. Replace Words — Medium
# https://leetcode.com/problems/replace-words/
# Submission 2198896906 — Accepted, Python3
#
# My thinking: every word is replaced by the
# shortest root that starts it. I try each prefix
# of the word, shortest first, and stop at the
# first one that appears in the dictionary.

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        result = []
        for word in sentence.split(" "):
            replacement = word
            for i in range(1, len(word) + 1):
                if word[:i] in roots:
                    replacement = word[:i]
                    break
            result.append(replacement)
        return " ".join(result)
