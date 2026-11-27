# LeetCode 3999. Minimum Number of String Groups Through Transformations — Hard
# https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/
# Submission 2203502868 — Accepted, Python3
from typing import List


class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        # My thinking: a transformation rotates the
        # even-index subsequence and the odd-index
        # subsequence independently, so two words are
        # equivalent exactly when their even parts are
        # rotations of each other and their odd parts are
        # rotations of each other. Rotation is an
        # equivalence relation, so each group is one
        # equivalence class: canonicalise every word by
        # its least lexicographic rotation of each part
        # (Booth's algorithm, linear time) and count the
        # distinct keys. Words of different lengths can
        # never collide, since the rotated parts keep
        # their lengths.
        def least_rotation(s: str) -> str:
            n = len(s)
            if n == 0:
                return ""
            ss = s + s
            i, j, k = 0, 1, 0
            while i < n and j < n and k < n:
                a, b = ss[i + k], ss[j + k]
                if a == b:
                    k += 1
                elif a < b:
                    j = j + k + 1
                    k = 0
                else:
                    i = i + k + 1
                    k = 0
                if i == j:
                    i += 1
            start = min(i, j)
            return ss[start:start + n]

        keys = set()
        for w in words:
            keys.add((least_rotation(w[0::2]), least_rotation(w[1::2])))
        return len(keys)
