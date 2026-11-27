# LeetCode 4091. Count Magical Substring Pairs II — Hard
# https://leetcode.com/problems/count-magical-substring-pairs-ii/
# Submission 2203707718 — Accepted, Python3
import operator
from array import array


class Solution:
    def countMagicalPairs(self, s: str) -> int:
        # My thinking: fix the split point j. The left
        # part s[i..j] and the right part s[j+1..k] are
        # magical when they have the same number of
        # distinct characters. As i moves left from j,
        # the distinct count of the left part only grows
        # at the last occurrence of each letter, and as
        # k moves right from j+1, the distinct count of
        # the right part only grows at the first
        # occurrence of each letter. So for each j, sort
        # the last occurrences of all letters to get the
        # lengths L[d] of the i-ranges where the left
        # part has exactly d distinct characters, and
        # precompute (scanning starts from the right)
        # the matching R[j][d] for the k-ranges where
        # the right part has exactly d distinct
        # characters. The answer for this j is the dot
        # product of L and R over d, summed over all j.
        n = len(s)
        a = [ord(ch) - 97 for ch in s]
        R = array('i', [0]) * (n * 26)
        first = [n] * 26
        for start in range(n - 1, 0, -1):
            first[a[start]] = start
            q = sorted(first)
            q.append(n)
            diffs = [q[i + 1] - q[i] for i in range(26)]
            base = (start - 1) * 26
            R[base:base + 26] = array('i', diffs)
        ans = 0
        last = [-1] * 26
        for j in range(n - 1):
            last[a[j]] = j
            p = sorted(last, reverse=True)
            p.append(-1)
            L = [p[i] - p[i + 1] if p[i] >= 0 else 0 for i in range(26)]
            base = j * 26
            ans += sum(map(operator.mul, L, R[base:base + 26]))
        return ans
