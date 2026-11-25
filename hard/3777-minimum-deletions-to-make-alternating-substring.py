# LeetCode 3777. Minimum Deletions to Make Alternating Substring — Hard
# https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/
# Submission 2203173689 — Accepted, Python3
from typing import List


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix(self, i: int) -> int:
        # My thinking: sum of the stored values at positions
        # 1..i (1-based), used for range sums below.
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        # My thinking: to make a string alternating by deleting
        # characters, every maximal run of equal letters of
        # length L must lose L - 1 of them, and that is exactly
        # the number of adjacent equal pairs inside the run.
        # So the deletions a substring needs equal the count of
        # positions i in [l, r-1] with s[i] == s[i+1]. Keep
        # those pair indicators in a Fenwick tree: a type-2
        # query is one range sum, and flipping s[j] only
        # changes the pairs ending at j-1 and j, so a type-1
        # query is two point updates.
        n = len(s)
        s = list(s)
        bad = [0] * max(n - 1, 0)
        bit = Fenwick(max(n - 1, 1))
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                bad[i] = 1
                bit.add(i + 1, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                s[j] = "B" if s[j] == "A" else "A"
                for i in (j - 1, j):
                    if 0 <= i < n - 1:
                        new = 1 if s[i] == s[i + 1] else 0
                        if new != bad[i]:
                            bit.add(i + 1, new - bad[i])
                            bad[i] = new
            else:
                l, r = q[1], q[2]
                # Pairs bad[l..r-1] sit at Fenwick positions
                # l+1..r, so the range sum is prefix(r) -
                # prefix(l).
                ans.append(bit.prefix(r) - bit.prefix(l))
        return ans
