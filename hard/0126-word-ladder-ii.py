# LeetCode 126. Word Ladder II — Hard
# https://leetcode.com/problems/word-ladder-ii/
# Submission 2198386680 — Accepted, Python3
#
# My thinking: I first walk out from the start word
# level by level, noting how far each word is and
# which words lead into it — stopping once the end
# word's level is finished, so I only keep shortest
# routes. Then I walk backwards from the end word
# through those parents, building every shortest
# ladder one step at a time.

from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        dist = {beginWord: 0}
        parents = defaultdict(list)
        queue = deque([beginWord])
        found = False
        while queue and not found:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + ch + word[i + 1:]
                        if nxt not in words:
                            continue
                        if nxt not in dist:
                            dist[nxt] = dist[word] + 1
                            parents[nxt].append(word)
                            queue.append(nxt)
                            if nxt == endWord:
                                found = True
                        elif dist[nxt] == dist[word] + 1:
                            parents[nxt].append(word)
        if endWord not in dist:
            return []
        paths = []

        def build(word: str, path: List[str]) -> None:
            if word == beginWord:
                paths.append([beginWord] + path[::-1])
                return
            for parent in parents[word]:
                build(parent, path + [word])

        build(endWord, [])
        return paths
