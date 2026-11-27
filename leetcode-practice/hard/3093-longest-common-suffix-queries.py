# LeetCode 3093. Longest Common Suffix Queries — Hard
# https://leetcode.com/problems/longest-common-suffix-queries/
# Submission 2201985382 — Accepted, Python3
#
# My thinking: I build a trie of the
# container words spelled backwards, so
# walking it follows a common suffix.
# Each node remembers the shortest
# container word passing through it
# (earliest on a tie). A query walks
# the reversed trie as far as it
# matches and takes the word stored
# at the deepest node reached.

from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        lengths = [len(w) for w in wordsContainer]
        children = [{}]
        best = [-1]

        def update(node, i):
            b = best[node]
            if b == -1 or lengths[i] < lengths[b]:
                best[node] = i

        for i, w in enumerate(wordsContainer):
            node = 0
            update(node, i)
            for ch in reversed(w):
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    best.append(-1)
                node = nxt
                update(node, i)
        ans = []
        for q in wordsQuery:
            node = 0
            for ch in reversed(q):
                nxt = children[node].get(ch)
                if nxt is None:
                    break
                node = nxt
            ans.append(best[node])
        return ans
