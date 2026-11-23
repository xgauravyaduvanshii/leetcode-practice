# LeetCode 3031. Minimum Time to Revert Word to Initial State II — Hard
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
# Submission 2201903326 — Accepted, Python3
#
# My thinking: after t seconds the word
# is its tail from t*k onwards plus any
# t*k letters I choose, so it can match
# the original exactly when that tail
# equals the matching head of the word.
# I find every such shift at once with
# the Z-function, which tells me how
# far the word matches itself at each
# spot, and take the earliest second
# that works (or the one that replaces
# the whole word).

from typing import List


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        # z[i]: longest prefix of word matching word[i:].
        z = [0] * n
        left = right = 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and word[z[i]] == word[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1
        t = 1
        while True:
            s = t * k
            if s >= n or z[s] >= n - s:
                return t
            t += 1
