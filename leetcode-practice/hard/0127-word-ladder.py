# LeetCode 127. Word Ladder — Hard
# https://leetcode.com/problems/word-ladder/
# Submission 2198387302 — Accepted, Python3
#
# My thinking: the shortest ladder is a shortest
# path, so I search level by level from the start
# word. Each step changes one letter to any other
# letter and keeps only words that are in the list
# and not visited yet. The first time I reach the
# end word, the number of steps so far is the
# answer; if the queue runs out, there is no ladder.

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words and nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
        return 0
