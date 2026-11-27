# LeetCode 3518. Smallest Palindromic Rearrangement II — Hard
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
# Submission 2202793462 — Accepted, Python3
from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # My thinking: a palindromic permutation is fixed by its first
        # half, which is a permutation of the halved character counts
        # (the odd-count letter, if any, sits in the middle). I first
        # check whether there are at least k distinct first halves at
        # all — if not, the answer is empty. Otherwise I build the
        # first half greedily, trying letters from 'a' upward and
        # taking a letter only when the permutations of what is left
        # are at least k; if fewer, I skip that many and move on.
        # Counts are capped at k + 1, since only the comparison with
        # k ever matters.
        cnt = Counter(s)
        half = {}
        mid = ""
        for ch in sorted(cnt):
            half[ch] = cnt[ch] // 2
            if cnt[ch] % 2 == 1:
                mid = ch
        m = sum(half.values())
        LIMIT = k + 1

        def count_perms(counts):
            res = 1
            remaining = sum(counts.values())
            for ch in sorted(counts):
                c = counts[ch]
                if c == 0:
                    continue
                b = 1
                cc = min(c, remaining - c)
                for i in range(1, cc + 1):
                    b = b * (remaining - cc + i) // i
                    if b > LIMIT:
                        b = LIMIT + 1
                        break
                if b > LIMIT:
                    return LIMIT
                res = res * b
                if res >= LIMIT:
                    return LIMIT
                remaining -= c
            return res

        if count_perms(half) < k:
            return ""
        first = []
        rem = dict(half)
        for _ in range(m):
            for ch in sorted(rem):
                if rem[ch] == 0:
                    continue
                rem[ch] -= 1
                c = count_perms(rem)
                if c >= k:
                    first.append(ch)
                    break
                k -= c
                rem[ch] += 1
        fh = "".join(first)
        return fh + mid + fh[::-1]
