# LeetCode 2213. Longest Substring of One Repeating Character — Hard
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/
# Submission 2201623725 — Accepted, Python3
#
# My thinking: the string is a row of runs
# of equal letters — each query splits one
# run, drops a single letter in, and lets it
# join its neighbours, while a heap keeps
# the longest run on top.

import bisect
import heapq
from collections import Counter


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        s = list(s)
        segs = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            segs.append([i, j])
            i = j + 1
        cnt = Counter()
        heap = []
        for l, r in segs:
            length = r - l + 1
            cnt[length] += 1
            heapq.heappush(heap, -length)

        def add_seg(l, r):
            length = r - l + 1
            cnt[length] += 1
            heapq.heappush(heap, -length)

        def remove_seg(l, r):
            cnt[r - l + 1] -= 1

        def current_max():
            while heap and cnt[-heap[0]] == 0:
                heapq.heappop(heap)
            return -heap[0] if heap else 0

        ans = []
        for idx, ch in zip(queryIndices, queryCharacters):
            if s[idx] != ch:
                pos = bisect.bisect_right(segs, idx, key=lambda seg: seg[0]) - 1
                l, r = segs.pop(pos)
                remove_seg(l, r)
                left_piece = [l, idx - 1] if l <= idx - 1 else None
                right_piece = [idx + 1, r] if idx + 1 <= r else None
                s[idx] = ch
                new_l, new_r = idx, idx
                if left_piece is None and pos > 0 and s[segs[pos - 1][1]] == ch:
                    ll, rr = segs.pop(pos - 1)
                    remove_seg(ll, rr)
                    new_l = ll
                    pos -= 1
                if right_piece is None and pos < len(segs) and s[segs[pos][0]] == ch:
                    ll, rr = segs.pop(pos)
                    remove_seg(ll, rr)
                    new_r = rr
                pieces = []
                if left_piece is not None:
                    pieces.append(left_piece)
                pieces.append([new_l, new_r])
                if right_piece is not None:
                    pieces.append(right_piece)
                segs[pos:pos] = pieces
                for pl, pr in pieces:
                    add_seg(pl, pr)
            ans.append(current_max())
        return ans
