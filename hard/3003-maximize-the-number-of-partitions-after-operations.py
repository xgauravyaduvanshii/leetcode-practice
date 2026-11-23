# LeetCode 3003. Maximize the Number of Partitions After Operations — Hard
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
# Submission 2201874037 — Accepted, Python3
#
# My thinking: I first cut the string
# the greedy way, into the longest
# pieces with at most k different
# letters. Then, for a change at one
# spot, I work out where the first new
# cut falls — the moment the piece
# holds k different letters and the
# changed letter still shows up
# elsewhere — and I count the pieces
# from there on with a table of how
# many pieces the untouched string
# still makes from every position. A
# change at the very start of a piece
# only counts when the fresh letter is
# one the previous piece cannot swallow.

from collections import Counter


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        if k == 26:
            return 1
        # Greedy partition: longest prefixes with at most k distinct letters.
        segs = []
        i = 0
        while i < n:
            seen = set()
            j = i
            while j < n and (s[j] in seen or len(seen) < k):
                seen.add(s[j])
                j += 1
            segs.append((i, j - 1))
            i = j
        base = len(segs)
        # nxt[i]: end of the longest prefix starting at i with <= k distinct.
        nxt = [0] * n
        cnt: Counter = Counter()
        r = -1
        for i in range(n):
            if r < i - 1:
                r = i - 1
                cnt.clear()
            while r + 1 < n and (s[r + 1] in cnt or len(cnt) < k):
                r += 1
                cnt[s[r]] += 1
            nxt[i] = r
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                del cnt[s[i]]
        # dp[i]: pieces the untouched string still makes from i onwards.
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[nxt[i] + 1]
        # kth[i]: first t >= i with distinct(s[i..t]) == k, or -1.
        kth = [-1] * n
        cnt = Counter()
        r = -1
        for i in range(n):
            if r < i - 1:
                r = i - 1
                cnt.clear()
            while r + 1 < n and len(cnt) < k:
                r += 1
                cnt[s[r]] += 1
            if len(cnt) == k:
                kth[i] = r
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                del cnt[s[i]]
        best = base
        for idx, (l, rseg) in enumerate(segs):
            distinct = set(s[l:rseg + 1])
            prev = set(s[segs[idx - 1][0]:segs[idx - 1][1] + 1]) if idx > 0 else set()
            # tstar: first spot in the piece where k different letters
            # have shown up; first/second: where each letter occurs.
            tstar = -1
            seen = set()
            for t in range(l, rseg + 1):
                seen.add(s[t])
                if tstar < 0 and len(seen) == k:
                    tstar = t
            if tstar < 0:
                continue
            first = {}
            second = {}
            for t in range(l, rseg + 1):
                ch = s[t]
                if ch not in first:
                    first[ch] = t
                elif ch not in second:
                    second[ch] = t
            for p in range(l, rseg + 1):
                ch = s[p]
                if first[ch] != p:
                    v = first[ch]
                elif ch in second:
                    v = second[ch]
                else:
                    continue  # the letter is unique here: no cut at all
                # The first new cut falls where the piece already holds
                # k letters, the change has happened, and the changed
                # letter still shows up somewhere else.
                cut_t = max(tstar, p, v)
                if cut_t == p:
                    # The piece cuts just before p; the next piece
                    # starts at p with the fresh letter.
                    w = kth[p + 1] if p + 1 < n else -1
                    gain = 2 + dp[w] - dp[l] if w >= 0 else 2 - dp[l]
                    if gain > 0:
                        best = max(best, base + gain)
                else:
                    # The piece cuts inside itself at cut_t; everything
                    # from there on is untouched.
                    if p == l and len(distinct | prev) >= 26:
                        continue
                    gain = 1 + dp[cut_t] - dp[l]
                    if gain > 0:
                        best = max(best, base + gain)
        return best
