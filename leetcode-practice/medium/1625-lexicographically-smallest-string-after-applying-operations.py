# LeetCode 1625. Lexicographically Smallest String After Applying Operations — Medium
# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
# Submission 2199894633 — Accepted, Python3
#
# My thinking: adding a to the odd positions
# and rotating are the only moves, and the
# string is short. I explore every reachable
# string breadth-first and keep the smallest.

from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = {s}
        queue = deque([s])
        best = s
        while queue:
            current = queue.popleft()
            best = min(best, current)
            added = "".join(str((int(ch) + a) % 10) if i % 2 == 1 else ch for i, ch in enumerate(current))
            if added not in seen:
                seen.add(added)
                queue.append(added)
            rotated = current[-b:] + current[:-b] if b else current
            if rotated not in seen:
                seen.add(rotated)
                queue.append(rotated)
        return best
