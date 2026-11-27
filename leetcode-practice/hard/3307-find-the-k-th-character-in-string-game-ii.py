# LeetCode 3307. Find the K-th Character in String Game II — Hard
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/
# Submission 2202315118 — Accepted, Python3
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # My thinking: the word doubles at every operation, so I only need the
        # lengths up to k (capped, since anything past k behaves the same). I
        # find the first operation where the word reaches k characters, then
        # walk backwards: whenever k falls in the appended half, I subtract
        # the length before that operation, and if the operation was type 1
        # (append the shifted copy) the character I am looking for was shifted
        # once more. Starting from 'a' plus the total shift gives the answer.
        lengths = [1]
        for op in operations:
            nxt = lengths[-1] * 2
            if nxt > k:
                nxt = k + 1
            lengths.append(nxt)
            if nxt > k:
                break
        j = 0
        while lengths[j] < k:
            j += 1
        shift = 0
        pos = k
        for i in range(j - 1, -1, -1):
            if pos > lengths[i]:
                pos -= lengths[i]
                if operations[i] == 1:
                    shift += 1
        return chr(ord("a") + shift % 26)
