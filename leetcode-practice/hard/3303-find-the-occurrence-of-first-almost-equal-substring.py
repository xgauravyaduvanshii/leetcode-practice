# LeetCode 3303. Find the Occurrence of First Almost Equal Substring — Hard
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/
# Submission 2202313273 — Accepted, Python3
from typing import List


class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        # My thinking: a start i works when s[i:i+m] matches pattern in all but
        # at most one position. I find the longest matching prefix of pattern
        # at i with a Z-function on pattern + '#' + s, and the longest matching
        # suffix with a Z-function on the reversed strings. If the prefix match
        # plus the suffix match covers at least m - 1 positions, the uncovered
        # middle is at most one character, so the start is valid. I scan starts
        # from the left and return the first valid one.
        n, m = len(s), len(pattern)

        def z_function(t: str) -> List[int]:
            z = [0] * len(t)
            left = right = 0
            for i in range(1, len(t)):
                if i <= right:
                    z[i] = min(right - i + 1, z[i - left])
                while i + z[i] < len(t) and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > right:
                    left, right = i, i + z[i] - 1
            return z

        z_forward = z_function(pattern + "#" + s)
        z_reverse = z_function(pattern[::-1] + "#" + s[::-1])
        for i in range(n - m + 1):
            prefix = min(z_forward[m + 1 + i], m)
            # The suffix of s[i:i+m], reversed, starts at n - (i + m) in s[::-1].
            suffix = min(z_reverse[m + 1 + n - (i + m)], m)
            if prefix + suffix >= m - 1:
                return i
        return -1
