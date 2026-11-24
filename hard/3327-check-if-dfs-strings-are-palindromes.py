# LeetCode 3327. Check if DFS Strings Are Palindromes — Hard
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
# Submission 2202375774 — Accepted, Python3
from typing import List

MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 9113823


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        # My thinking: the DFS string of a node is the concatenation of its
        # children's DFS strings (children in increasing order) followed by
        # its own character, so in one post-order walk of the whole tree
        # each subtree occupies one contiguous interval, ending at the node's
        # own position. I record that interval per node, then answer every
        # palindrome query in O(1) with a double rolling hash: a substring
        # is a palindrome exactly when its forward hash equals the hash of
        # the same interval read on the reversed string.
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        order = []  # post-order characters
        pos = [0] * n
        size = [0] * n
        stack = [(0, False)]
        while stack:
            u, done = stack.pop()
            if done:
                pos[u] = len(order)
                order.append(s[u])
                size[u] = 1 + sum(size[c] for c in children[u])
            else:
                stack.append((u, True))
                for c in reversed(children[u]):
                    stack.append((c, False))

        t = ''.join(order)
        rev = t[::-1]

        def build_hashes(text):
            h1 = [0] * (n + 1)
            h2 = [0] * (n + 1)
            for i, ch in enumerate(text):
                v = ord(ch)
                h1[i + 1] = (h1[i] * BASE + v) % MOD1
                h2[i + 1] = (h2[i] * BASE + v) % MOD2
            return h1, h2

        h1, h2 = build_hashes(t)
        r1, r2 = build_hashes(rev)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = pow1[i - 1] * BASE % MOD1
            pow2[i] = pow2[i - 1] * BASE % MOD2

        def get(h, p, mod, l, r):
            return (h[r + 1] - h[l] * p[r - l + 1]) % mod

        ans = []
        for u in range(n):
            l = pos[u] - size[u] + 1
            r = pos[u]
            rl = n - 1 - r
            rr = n - 1 - l
            ok = (get(h1, pow1, MOD1, l, r) == get(r1, pow1, MOD1, rl, rr)
                  and get(h2, pow2, MOD2, l, r) == get(r2, pow2, MOD2, rl, rr))
            ans.append(ok)
        return ans
