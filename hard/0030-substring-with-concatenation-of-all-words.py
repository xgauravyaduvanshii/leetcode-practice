# LeetCode 30. Substring with Concatenation of All Words — Hard
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Submission 2198363805 — Accepted, Python3
#
# My thinking: every word has the same length, so a
# match is just a run of whole words back to back.
# I slide a window in word-sized steps, trying each
# starting offset within one word. Inside the window
# I count the words I see; a word I have seen too
# many of shrinks the window from the left, and a
# word that is not in the list restarts it entirely.

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        need = Counter(words)
        answer = []
        for start in range(word_len):
            left = start
            seen = Counter()
            matched = 0
            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word in need:
                    seen[word] += 1
                    matched += 1
                    while seen[word] > need[word]:
                        seen[s[left:left + word_len]] -= 1
                        matched -= 1
                        left += word_len
                    if matched == word_count:
                        answer.append(left)
                else:
                    seen.clear()
                    matched = 0
                    left = right + word_len
        return answer
