# LeetCode 3816. Lexicographically Smallest String After Deleting Duplicate Characters — Hard
# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/
# Submission 2203192731 — Accepted, Python3
from bisect import bisect_left


class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        # My thinking: deleting an occurrence is only allowed
        # while its letter still appears at least twice, so
        # every distinct letter must survive at least once,
        # and any subsequence keeping each distinct letter at
        # least once can be reached by deleting the rest one
        # by one. So the task is the lexicographically smallest
        # subsequence of s that contains every distinct letter
        # at least once. I build it left to right: at each
        # step I take the smallest letter that occurs at or
        # after the current position and still leaves every
        # not-yet-taken letter occurring after the chosen spot.
        # A letter is safe exactly when its position lies
        # before the last occurrence of every still-missing
        # letter except possibly its own, so I keep the
        # smallest and second smallest such last occurrences
        # and test each candidate against them in O(1); the
        # earliest occurrence of the chosen letter (found by
        # binary search) leaves the longest suffix, so the
        # choice is safe. Once every distinct letter is taken
        # I stop — appending anything more would only make
        # the string longer with the same prefix, hence
        # larger. A feasible candidate always exists: the
        # still-missing letter whose first occurrence from
        # here is earliest can always be taken next.
        positions = [[] for _ in range(26)]
        last = [-1] * 26
        for i, c in enumerate(s):
            o = ord(c) - 97
            positions[o].append(i)
            last[o] = i
        distinct = [o for o in range(26) if positions[o]]
        missing = set(distinct)
        taken = set()
        # Smallest and second smallest last occurrence among
        # the letters still missing; recomputed only when a
        # letter is taken, since the missing set only shrinks
        # then. (Last occurrences are distinct positions, so
        # the smallest one belongs to exactly one letter.)
        m1 = m2 = float("inf")
        argm1 = -1

        def refresh():
            nonlocal m1, m2, argm1
            m1 = m2 = float("inf")
            argm1 = -1
            for d in missing:
                if last[d] < m1:
                    m2 = m1
                    m1 = last[d]
                    argm1 = d
                elif last[d] < m2:
                    m2 = last[d]

        refresh()
        pos = 0
        ans = []
        while len(taken) < len(distinct):
            for c in range(26):
                arr = positions[c]
                k = bisect_left(arr, pos)
                if k == len(arr):
                    continue
                p = arr[k]
                threshold = m2 if c == argm1 else m1
                if p < threshold:
                    ans.append(chr(c + 97))
                    taken.add(c)
                    pos = p + 1
                    if c in missing:
                        missing.discard(c)
                        refresh()
                    break
        return "".join(ans)
