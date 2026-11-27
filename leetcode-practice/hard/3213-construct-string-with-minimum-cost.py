# LeetCode 3213. Construct String with Minimum Cost — Hard
# https://leetcode.com/problems/construct-string-with-minimum-cost/
# Submission 2202095055 — Accepted, Python3
#
# My thinking: I dedupe the words, keeping
# the cheapest cost per word, then run a
# DP over the target: dp[i] is the cheapest
# cost to build the first i characters.
# Matching words at each position is a
# trie walk, except when words are very
# long — then I precompute every
# occurrence with string search instead.
# The hybrid keeps both the long-word and
# the many-occurrence cases inside the
# limits.

from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        best = {}
        for w, c in zip(words, costs):
            if w not in best or c < best[w]:
                best[w] = c
        n = len(target)
        INF = 10 ** 18
        dp = [INF] * (n + 1)
        dp[0] = 0
        max_len = 0
        for w in best:
            if len(w) > max_len:
                max_len = len(w)
        use_find = False
        if max_len > 300:
            # Upper bound on overlapping occurrences; str.count
            # undercounts overlapping matches, so use this instead.
            total = 0
            for w in best:
                L = len(w)
                if L <= n:
                    total += n - L + 1
                if total > 1500000:
                    break
            if total <= 1500000:
                use_find = True
        if use_find:
            trans = [[] for _ in range(n)]
            find = target.find
            for w, c in best.items():
                L = len(w)
                if L > n:
                    continue
                start = 0
                while True:
                    idx = find(w, start)
                    if idx < 0:
                        break
                    trans[idx].append((idx + L, c))
                    start = idx + 1
            for i in range(n):
                di = dp[i]
                if di == INF:
                    continue
                for j, c in trans[i]:
                    nd = di + c
                    if nd < dp[j]:
                        dp[j] = nd
            return dp[n] if dp[n] != INF else -1
        children = [{}]
        end = [-1]
        for w, c in best.items():
            node = 0
            for ch in w:
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    end.append(-1)
                node = nxt
            if end[node] == -1 or c < end[node]:
                end[node] = c
        for i in range(n):
            di = dp[i]
            if di == INF:
                continue
            node = 0
            upper = i + max_len
            if upper > n:
                upper = n
            for j in range(i, upper):
                nxt = children[node].get(target[j])
                if nxt is None:
                    break
                node = nxt
                c = end[node]
                if c != -1:
                    nd = di + c
                    if nd < dp[j + 1]:
                        dp[j + 1] = nd
        return dp[n] if dp[n] != INF else -1
