# LeetCode 3485. Longest Common Prefix of K Strings After Removal — Hard
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/
# Submission 2202697673 — Accepted, Python3

from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        # My thinking: the answer for the whole array is the deepest
        # trie node whose subtree holds at least k words, call that
        # depth D. Removing one word can only hurt a node on that
        # word's own path, and only if the node holds exactly k
        # words. So every answer is D unless the single deepest
        # k-node is unique and lies on the removed word's path.
        # For those words the answer is the best of two things: a
        # node holding at least k+1 words (it survives any single
        # removal), and the deepest k-node off the unique node's
        # root path (that path is shared by all such words, so one
        # value covers them all).
        n = len(words)
        children = [{}]
        cnt = [0]
        parent = [-1]
        word_nodes = []
        for w in words:
            node = 0
            path = [0]
            for ch in w:
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    cnt.append(0)
                    parent.append(node)
                node = nxt
                cnt[node] += 1
                path.append(node)
            word_nodes.append(path)
        if n < k:
            return [0] * n
        depth = [0] * len(children)
        stack = [0]
        while stack:
            u = stack.pop()
            for v in children[u].values():
                depth[v] = depth[u] + 1
                stack.append(v)
        A = 0
        D = 0
        for node in range(1, len(children)):
            if cnt[node] >= k + 1:
                A = max(A, depth[node])
            if cnt[node] >= k:
                D = max(D, depth[node])
        sD = [node for node in range(1, len(children))
              if depth[node] == D and cnt[node] >= k]
        if len(sD) >= 2:
            return [D] * n
        if len(sD) == 0:
            return [0] * n
        u_star = sD[0]
        anc = set()
        cur = u_star
        while cur != -1:
            anc.add(cur)
            cur = parent[cur]
        B = 0
        for node in range(1, len(children)):
            if depth[node] < D and cnt[node] >= k and node not in anc:
                B = max(B, depth[node])
        ans = [0] * n
        for i, path in enumerate(word_nodes):
            ans[i] = max(A, B) if u_star in path else D
        return ans
